import asyncio
from typing import Callable
import websockets
import json
from dotenv import load_dotenv
from src.classes.logger import ServerLogger
from src.classes import utils
from src.classes.constants import AUDIO_SAMPLE_RATE

load_dotenv()
logger = utils.make_logger(name="WebSocketServer")


class WebSocketServer:
    def __init__(
            self,
            sample_rate,
            host="0.0.0.0",
            port=6789,
            started_cb: Callable[[str, int], None] | None = None,
            session_complete_cb: Callable[[str], None] | None = None,
    ):
        self.host = host
        self.port = int(port)
        self.sessions = {}
        self.system_clients: set[websockets.WebSocketServerProtocol] = set()
        self.server = None
        self.server_logger = ServerLogger(sample_rate)
        self.started_cb = started_cb
        self.session_complete_cb = session_complete_cb

    async def __aenter__(self):
        await self.start_server()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.stop_server()

    async def handler(self, websocket):
        session_id = None
        role = None
        try:
            init_msg = await websocket.recv()
            init_data = json.loads(init_msg)
            session_id = init_data.get("session_id")
            role = init_data.get("role")
            logger.debug(f"Role: {role}")
            raw = init_data.get("message")
            payload = json.loads(raw) if raw else {}

            if role == "system":
                self.system_clients.add(websocket)
                logger.debug("System client connected")

            if role == "runner":
                while True:
                    try:
                        message = await websocket.recv()
                        for sid, parts in self.sessions.items():
                            dbg_ws = parts.get("debugger")
                            if dbg_ws and dbg_ws is not websocket:
                                try:
                                    await dbg_ws.send(message)
                                except:
                                    pass

                        for sys_ws in list(self.system_clients):
                            if sys_ws is not websocket:
                                try:
                                    await sys_ws.send(message)
                                except:
                                    self.system_clients.discard(sys_ws)
                    except websockets.exceptions.ConnectionClosed:
                        break
                    except websockets.exceptions.ConnectionClosedOK:
                        break

            if role == "system":
                event = payload.get("event")
                if event == "benchforce.get_pending_sessions":
                    pending = [
                        sid for sid, parts in self.sessions.items()
                        if sum(1 for r in parts if r in ("client","agent")) == 1
                    ]
                    await websocket.send(json.dumps({"status": "success", "data": pending}))

                if event == "benchforce.current_sessions":
                    active_sessions = [
                        sid for sid, parts in self.sessions.items()
                        if "client" in parts or "agent" in parts
                    ]
                    await websocket.send(json.dumps({
                        "status": "success",
                        "data": active_sessions
                    }))

                return

            if not session_id or role not in ("client", "agent", "debugger"):
                await websocket.send(json.dumps({
                    "status": "error",
                    "error": "Invalid session_id or role"
                }))
                logger.warning(f"Invalid session_id or role: {init_data}")
                return

            if session_id not in self.sessions:
                self.sessions[session_id] = {}
                self.server_logger.register_session(session_id)

            self.sessions[session_id][role] = websocket
            logger.debug(f"{role} connected to session {session_id}")

            participants = self.sessions[session_id]
            if "client" in participants and "agent" in participants:
                logger.debug(f"Session {session_id} fully connected ({participants}).")

            skip_events = {
                "response.log_tts", "response.log_stt",
                "benchforce.log_original_db", "benchforce.log_dryrun_db"
            }

            while True:
                try:
                    message = await websocket.recv()
                    data = json.loads(message)
                    payload = json.loads(data.get("message", "{}"))
                    
                    # Add role information for audio tracking
                    data["role"] = role
                    self.server_logger.save_packet(session_id, data)

                    if payload.get("event") not in skip_events:
                        target = "agent" if role == "client" else "client"
                        ws_target = participants.get(target)
                        if ws_target:
                            await ws_target.send(message)
                        else:
                            await websocket.send(json.dumps({
                                "status": "error",
                                "error": f"{target} not connected"
                            }))
                            logger.warning(f"{target} not connected in session {session_id}")

                        dbg = participants.get("debugger")
                        if dbg:
                            await dbg.send(message)

                except websockets.exceptions.ConnectionClosedOK:
                    break
                except websockets.exceptions.ConnectionClosed:
                    break

        except websockets.exceptions.ConnectionClosedOK:
            pass
        except websockets.exceptions.ConnectionClosed:
            pass

        finally:
            if session_id in self.sessions and role in self.sessions[session_id]:
                del self.sessions[session_id][role]
                
                # Check if this was the last client or agent (not including debugger)
                remaining_roles = set(self.sessions[session_id].keys())
                logger.debug(f"Removing {role}. Remaining roles: {remaining_roles}")
                active_roles = remaining_roles & {"client", "agent"}
                
                if not active_roles:  # No more client or agent
                    logger.debug(f"No more client or agent; unregistering session...")
                    self.server_logger.unregister_session(session_id)
                    logger.debug(f"Session unregistered.")
                
                if not self.sessions[session_id]:  # Completely empty
                    del self.sessions[session_id]

                    if self.session_complete_cb is not None:
                        self.session_complete_cb(session_id)

            logger.debug(f"{role} disconnected from session {session_id}")

    async def start_server(self):
        self.server = await websockets.serve(
            self.handler,
            self.host,
            self.port,
            max_size=100 * 1024 * 1024,
            max_queue=1024,
            ping_interval=1,
            open_timeout=30,
            ping_timeout=60,  # WebSocket connection error in handle_judge_messages: received 1011 (internal error) keepalive ping timeout; then sent 1011 (internal error) keepalive ping timeout
            close_timeout=30,
            # logger=logger,
        )
        logger.debug(f"WebSocket server started at ws://{self.host}:{self.port}")
        if self.started_cb is not None:
            self.started_cb(self.host, self.port)
        await self.server.wait_closed()

    async def stop_server(self):
        if self.server:
            self.server.close()
            await self.server.wait_closed()
            logger.info("WebSocket server stopped.")


async def run_server_async(sample_rate=AUDIO_SAMPLE_RATE, host: str="0.0.0.0", port:int=6789):
    server = WebSocketServer(sample_rate, host=host, port=port)
    await server.start_server()


def run_server(sample_rate=AUDIO_SAMPLE_RATE, host: str="0.0.0.0", port:int=6789):
    server = WebSocketServer(sample_rate, host=host, port=port)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.create_task(server.start_server())
        loop.run_forever()
    except KeyboardInterrupt:
        loop.run_until_complete(server.stop_server())
    finally:
        loop.close()
