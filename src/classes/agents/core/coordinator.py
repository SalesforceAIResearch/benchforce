import base64
from typing import Dict, Any, Optional

from src.classes.utils import make_logger
from src.classes.agents.core.websocket_manager import WebSocketManager, WebSocketEventHandler
from src.classes.agents.core.agent import Agent, AgentResponse
from src.classes.agents.core.tool_processor import ToolProcessor
from src.classes.packet import UnifiedPacket, EventType

logger = make_logger(name="Coordinator")

CLIENT_ICON = "🕵️‍♀️"
CLIENT_NAME = "Client"


class Coordinator(WebSocketEventHandler):
    """
    Acts as the conversation coordinator between the given Agent and a Client whose messages come in
    via websockets managed by the given WebSocketManager.
    """
    
    def __init__(self, agent: Agent, config=None):
        self.agent = agent
        self.config = config

        self._websocket_manager = None
        self._tool_processor = None
        
        # Audio processing components (only initialized if needed)
        self.tts = None
        self.asr = None
        
    async def start(self, host: str = "localhost", port: int = 6789) -> None:
        """Start the provider coordinator and all its components"""
        try:
            # Initialize agent
            await self.agent.initialize()
            
            # Create WebSocket manager
            self._websocket_manager = WebSocketManager(
                session_id=self.agent.session_id,
                mode=self.agent.mode,
                event_handler=self  # This coordinator handles the events
            )
            
            # Create tool processor
            self._tool_processor = ToolProcessor(self._websocket_manager)
            
            # Initialize audio components if in voice mode
            if self.agent.mode == "voice":
                await self._initialize_audio_components()
            
            # Start WebSocket connection and processing
            await self._websocket_manager.connect(host=host, port=port)
            
        except Exception as e:
            logger.error(f"Error starting provider coordinator: {e}")
            await self.close()
            raise
    
    async def close(self) -> None:
        """Clean up all components"""
        try:
            if self.agent:
                await self.agent.close()
        except Exception as e:
            logger.error(f"Error during agent close: {e}")
            raise
        finally:
            try:
                if self._websocket_manager:
                    await self._websocket_manager.close()
            except Exception as e:
                logger.error(f"Error during websocket_manager close: {e}")
                raise
    
    def is_terminated(self) -> bool:
        """Check if the session is terminated"""
        if self._websocket_manager:
            return self._websocket_manager.is_terminated()
        return True
    
    # WebSocketEventHandler implementation
    
    async def handle_text_message(self, message_data: Dict[str, Any]) -> None:
        """Handle incoming text message"""
        client_text = message_data.get("text")
        if not client_text:
            logger.debug("Client sent an empty text message")
            return
        
        logger.info(f"{CLIENT_ICON} {CLIENT_NAME}: {client_text}")
        
        try:
            # Process message through agent
            agent_response = await self._get_agent_response(client_text=client_text)
            
            if not agent_response.text:
                logger.debug("Agent produced an empty response")
                return
            
            logger.info(f"{self.agent.AGENT_CONFIG.log_icon} {self.agent.AGENT_CONFIG.log_name}: {agent_response.text}")
            
            # Send tool notifications if any
            if agent_response.has_tools():
                await self._tool_processor.notify_tool_calls(agent_response.tool_calls)
            
            # Send text response
            await self._send_agent_text_response(agent_response.text)
            
        except Exception as e:
            logger.error(f"Error handling text message: {e}")
            # Send error response
            await self._send_agent_text_response("I apologize, but I encountered an error processing your message.")
    
    async def handle_audio_message(self, message_data: Dict[str, Any]) -> None:
        """Handle incoming audio message"""
        client_audio = message_data.get("audio")
        if not client_audio:
            logger.debug("Client sent an empty audio message")
            return
        
        try:
            # Convert audio to text
            if not self.asr:
                logger.error("ASR not initialized for voice mode")
                return
            
            client_text = self.asr.process_audio(audio_data=base64.b64decode(client_audio))
            if not client_text:
                logger.debug("ASR produced an empty text message from client audio")
                return
            
            logger.info(f"{CLIENT_ICON} {CLIENT_NAME}: {client_text}")
            
            # Send STT log
            await self._websocket_manager.send_packet(
                UnifiedPacket(event=EventType.RESPONSE_LOG_STT, text=client_text)
            )
            
            # Process message through agent
            agent_response = await self._get_agent_response(client_text=client_text)
            
            if not agent_response.text:
                logger.debug("Agent produced an empty response")
                return
            
            logger.info(f"{self.agent.AGENT_CONFIG.log_icon} {self.agent.AGENT_CONFIG.log_name}: {agent_response.text}")
            
            # Send tool notifications if any
            if agent_response.has_tools():
                await self._tool_processor.notify_tool_calls(agent_response.tool_calls)
            
            # Convert response to audio and send
            await self._send_agent_audio_response(agent_response.text)
            
        except Exception as e:
            logger.error(f"Error handling audio message: {e}")
            # Send error audio response
            await self._send_agent_audio_response("I apologize, but I encountered an error processing your message.")
    
    async def handle_custom_event(self, event_type: str, message_data: Dict[str, Any]) -> bool:
        """Handle custom events not handled by base WebSocket manager"""
        # Allow agents to handle custom events if they want
        # For now, just log unhandled events
        logger.debug(f"Unhandled custom event: {event_type}")
        return False
    
    # Private methods
    
    async def _get_agent_response(self, client_text: str) -> AgentResponse:
        """Process user input through the agent"""
        # Pre-process text
        processed_input = await self.agent.pre_process_text(client_text)
        
        # Get agent response
        response = await self.agent.process_message(processed_input)
        
        # Post-process text
        if response.text:
            response.text = await self.agent.post_process_text(response.text)
        
        # Check if agent wants to terminate
        if self.agent.should_terminate():
            self._websocket_manager.session_terminated = True
        
        return response
    
    async def _send_agent_text_response(self, text: str) -> None:
        """Send text response to client"""
        await self._websocket_manager.send_packet(
            UnifiedPacket(event=EventType.RESPONSE_TEXT_DONE, text=text)
        )
        await self._websocket_manager.send_packet(
            UnifiedPacket(event=EventType.RESPONSE_DONE)
        )
    
    async def _send_agent_audio_response(self, text: str) -> None:
        """Send audio response to client"""
        if not self.tts:
            logger.error("TTS not initialized for voice mode")
            return
        
        # Convert text to audio
        audio_response_bytes = self.tts.process(text)
        audio_response = base64.b64encode(bytes(audio_response_bytes)).decode("utf-8")
        
        # Send TTS log
        await self._websocket_manager.send_packet(
            UnifiedPacket(event=EventType.RESPONSE_LOG_TTS, text=text)
        )
        
        # Send audio transcript
        await self._websocket_manager.send_packet(
            UnifiedPacket(event=EventType.RESPONSE_AUDIO_TRANSCRIPT_DONE, text=text)
        )
        
        # Send audio response
        await self._websocket_manager.send_packet(
            UnifiedPacket(event=EventType.RESPONSE_AUDIO_DONE, audio=audio_response)
        )
        
        # Send done signal
        await self._websocket_manager.send_packet(
            UnifiedPacket(event=EventType.RESPONSE_DONE)
        )
    
    async def _initialize_audio_components(self) -> None:
        """Initialize TTS and ASR components for voice mode"""
        try:
            from src.classes.providers.elevenlabs import ElevenlabsTTS
            from src.classes.providers.deepgram import DeepgramSTT
            from src.classes.constants import AUDIO_SAMPLE_RATE
            
            # Use config values or fallback to defaults
            tts_model = self.config.agent_tts_model if self.config else "eleven_multilingual_v2"
            tts_voice = self.config.agent_tts_voice if self.config else "qBDvhofpxp92JgXJxDjB"
            stt_model = self.config.agent_stt_model if self.config else "nova-3"
            
            self.tts = ElevenlabsTTS(
                model=tts_model,
                sample_rate=AUDIO_SAMPLE_RATE,
                voice=tts_voice,
            )
            
            self.asr = DeepgramSTT(base_model=stt_model)
            
            logger.debug(f"Audio components initialized: TTS={tts_model}, Voice={tts_voice}, STT={stt_model}")
            
        except ImportError as e:
            logger.error(f"Failed to import audio components: {e}")
            raise
        except Exception as e:
            logger.error(f"Failed to initialize audio components: {e}")
            raise
