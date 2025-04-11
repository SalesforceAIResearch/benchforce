import asyncio
import websockets
import json
import os
from dotenv import load_dotenv
from src.classes.logger import ServerLogger

load_dotenv()

class WebSocketServer:
    def __init__(self, sample_rate, host="127.0.0.1", port=os.environ.get("WS_SERVER_PORT", 6789)):
        self.host = host
        self.port = int(port)
        self.sessions = {}
        self.server = None
        self.logger = ServerLogger(sample_rate)

    async def handler(self, websocket):
        session_id = None
        role = None
        try:
            message = await websocket.recv()
            data = json.loads(message)
            session_id = data.get("session_id")
            role = data.get("role")
            if not session_id or role not in ["client", "agent"]:
                await websocket.send(json.dumps({"status": "error", "error": "Invalid session_id or role"}))
                self.logger.warning(f"Invalid session_id or role: {data}")
                return
            if session_id not in self.sessions:
                self.sessions[session_id] = {}
                self.logger.register_session(session_id)
            self.sessions[session_id][role] = websocket
            if "client" in self.sessions[session_id] and "agent" in self.sessions[session_id]:
                self.logger.info(f"Session {session_id} fully connected.")
            while True:
                try:
                    message = await websocket.recv()
                    data = json.loads(message)
                    payload = json.loads(data.get("message"))
                    self.logger.save_packet(session_id, data)
                    if session_id in self.sessions and payload.get("event") not in ["response.log_tts", "response.log_stt", "benchforce.log_original_db", "benchforce.log_dryrun_db"]:
                        target_role = "agent" if role == "client" else "client"
                        target_ws = self.sessions[session_id].get(target_role)
                        if target_ws:
                            await target_ws.send(message)
                        else:
                            await websocket.send(json.dumps({
                                "status": "error", 
                                "error": f"{target_role} not connected"
                            }))
                            self.logger.warning(f"{target_role} not connected in session {session_id}")
                except websockets.exceptions.ConnectionClosed:
                    break
        finally:
            if session_id in self.sessions and role in self.sessions[session_id]:
                del self.sessions[session_id][role]
                if not self.sessions[session_id]:
                    del self.sessions[session_id]
                    self.logger.unregister_session(session_id)
            self.logger.info(f"{role} disconnected from session {session_id}")

    async def start_server(self):
        self.server = await websockets.serve(self.handler, self.host, self.port, max_size=100 * 1024 * 1024)
        self.logger.info(f"WebSocket server started at ws://{self.host}:{self.port}")
        await self.server.wait_closed()

    async def stop_server(self):
        if self.server:
            self.server.close()
            await self.server.wait_closed()
            self.logger.info("WebSocket server stopped.")

async def run_server_async(sample_rate):
    server = WebSocketServer(sample_rate)
    await server.start_server()

def run_server(sample_rate):
    server = WebSocketServer(sample_rate)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.create_task(server.start_server())
        loop.run_forever()
    except KeyboardInterrupt:
        loop.run_until_complete(server.stop_server())
    finally:
        loop.close()