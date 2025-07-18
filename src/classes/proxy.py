import json
import websockets
import asyncio


class ProxyClient:
    def __init__(self, uri: str, session_id: str, role: str):
        self.uri = uri
        self.session_id = session_id
        self.role = role
        self.ws = None

    async def connect(self):
        self.ws = await websockets.connect(self.uri, max_size=100 * 1024 * 1024, open_timeout=None, ping_timeout=None, close_timeout=None)

    async def send_message(self, message: str):
        if self.ws is None:
            raise Exception("Websocket connection not established.")
        payload = {
            "session_id": self.session_id,
            "role": self.role,
            "message": message
        }
        json_payload = json.dumps(payload)
        await self.ws.send(json_payload)

    async def close(self):
        if self.ws:
            asyncio.create_task(self.ws.close())
