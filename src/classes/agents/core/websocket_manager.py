import json
import websockets
from typing import Dict, Any, Optional
from abc import ABC, abstractmethod

from src.classes.utils import make_logger
from src.classes.packet import UnifiedPacket, EventType

logger = make_logger(name="WebSocketManager")


class WebSocketEventHandler(ABC):
    """Interface for handling websocket events"""
    
    @abstractmethod
    async def handle_text_message(self, message_data: Dict[str, Any]) -> None:
        """Handle incoming text message"""
        pass
    
    @abstractmethod
    async def handle_audio_message(self, message_data: Dict[str, Any]) -> None:
        """Handle incoming audio message"""
        pass
    
    @abstractmethod
    async def handle_custom_event(self, event_type: str, message_data: Dict[str, Any]) -> bool:
        """
        Handle custom events not handled by base class.
        
        Returns:
            True if event was handled, False if it should be ignored
        """
        pass


class WebSocketManager:
    """
    Manages WebSocket connection and handles common event processing.
    All boilerplate websocket logic is contained here.
    """
    
    def __init__(self, session_id: str, mode: str, event_handler: WebSocketEventHandler):
        self.session_id = session_id
        self.mode = mode
        self.event_handler = event_handler
        
        self.websocket: Optional[websockets.WebSocketServerProtocol] = None
        self.session_terminated = False
        
    async def connect(self, host: str = "localhost", port: int = 6789) -> None:
        """Connect to websocket server and handle all setup"""
        try:
            logger.debug(f"Connecting to WebSocket at {host}:{port}")
            
            # Establish connection
            self.websocket = await websockets.connect(
                f"ws://{host}:{port}",
                max_size=100 * 1024 * 1024,
                ping_interval=1,
                open_timeout=None,
                ping_timeout=None,
                close_timeout=None,
            )
            
            # Send initial handshake
            await self._send_handshake()
            
            # Send ready signal
            await self.send_packet(
                UnifiedPacket(event=EventType.BENCHFORCE_HANDSHAKE, text="agent_ready")
            )
            
            # Start message handling loop
            await self._handle_messages()
            
        except Exception as e:
            logger.error(f"Error in WebSocket connection: {e}")
            self.session_terminated = True
            raise
    
    async def send_packet(self, packet: UnifiedPacket) -> None:
        """Send a packet to the judge"""
        if not self.websocket:
            raise ConnectionError("WebSocket is not connected")
        
        payload = {
            "session_id": self.session_id,
            "role": "agent",
            "message": packet.to_json()
        }
        
        try:
            await self.websocket.send(json.dumps(payload))
            logger.debug(f"Sent packet: {packet.event}")
        except (websockets.exceptions.ConnectionClosed, AttributeError) as e:
            logger.error(f"WebSocket connection error: {e}")
            self.session_terminated = True
        except Exception as e:
            logger.error(f"Unexpected error sending packet: {e}")
            self.session_terminated = True
    
    async def close(self) -> None:
        """Close websocket connection"""
        if self.websocket and not self.websocket.closed:
            await self.websocket.close()
            logger.debug("WebSocket connection closed")
        self.websocket = None
    
    def is_terminated(self) -> bool:
        """Check if session is terminated"""
        return self.session_terminated
    
    async def _send_handshake(self) -> None:
        """Send initial handshake message"""
        await self.websocket.send(json.dumps({
            "session_id": self.session_id,
            "role": "agent",
            "message": ""
        }))
    
    async def _handle_messages(self) -> None:
        """Main message handling loop with common event processing"""
        try:
            async for message in self.websocket:
                try:
                    data = json.loads(message)
                    msg = json.loads(data.get("message", "{}"))
                    event = msg.get("event")
                    
                    logger.debug(f"Received event: {event} from {data.get('role')}")
                    
                    # Handle common events in base class
                    if await self._handle_common_event(event, msg):
                        continue
                    
                    # Route to specific handlers
                    await self._route_event(event, msg)
                    
                except json.JSONDecodeError as e:
                    logger.error(f"Error decoding message: {e}")
                    continue
                except Exception as e:
                    logger.error(f"Error in message handler: {e}")
                    self.session_terminated = True
                    break
        
        except (websockets.exceptions.ConnectionClosed, AttributeError) as e:
            logger.error(f"WebSocket connection error: {e}")
            self.session_terminated = True
        except Exception as e:
            logger.error(f"Unexpected error in message handling: {e}")
            self.session_terminated = True
    
    async def _handle_common_event(self, event: str, message_data: Dict[str, Any]) -> bool:
        """
        Handle common events that all providers need.
        
        Returns:
            True if event was handled, False if it should be routed to specific handlers
        """
        if event == EventType.BENCHFORCE_TERMINATE.value:
            logger.debug("Received termination signal")
            await self.send_packet(UnifiedPacket(event=EventType.BENCHFORCE_TERMINATE))
            self.session_terminated = True
            return True
        
        return False
    
    async def _route_event(self, event: str, message_data: Dict[str, Any]) -> None:
        """Route events to appropriate handlers"""
        if event == EventType.RESPONSE_TEXT_DONE.value and self.mode == "text":
            await self.event_handler.handle_text_message(message_data)
        elif event == EventType.RESPONSE_AUDIO_DONE.value and self.mode == "voice":
            await self.event_handler.handle_audio_message(message_data)
        else:
            # Let the handler decide if it wants to handle custom events
            handled = await self.event_handler.handle_custom_event(event, message_data)
            if not handled:
                logger.debug(f"Unhandled event: {event}")
