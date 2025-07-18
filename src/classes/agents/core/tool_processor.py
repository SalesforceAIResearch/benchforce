from typing import List
from src.classes.utils import make_logger
from src.classes.agents.core.agent import ToolCall
from src.classes.packet import UnifiedPacket, EventType

logger = make_logger(name="ToolProcessor")


class ToolProcessor:
    """
    Handles tool notification sending to WebSocket.
    Real tool execution happens in agents - this just sends notifications.
    """
    
    def __init__(self, websocket_manager):
        self.websocket_manager = websocket_manager
    
    async def notify_tool_calls(self, tool_calls: List[ToolCall]) -> None:
        """
        Send WebSocket notifications for tool calls.
        Agents handle the actual execution.
        
        Args:
            tool_calls: List of ToolCall objects to notify about
        """
        for tool_call in tool_calls:
            if self.websocket_manager.is_terminated():
                break
            
            try:
                # Send tool call notification
                await self._send_tool_call_notification(tool_call)
                
                # Send mock result notification (agents handle real results)
                await self._send_tool_result_notification(tool_call)
                
                # Handle special tool behaviors
                await self._handle_special_tool_behaviors(tool_call)
                
            except Exception as e:
                logger.error(f"Error sending tool notification {tool_call.name}: {e}")
    
    async def _send_tool_call_notification(self, tool_call: ToolCall) -> None:
        """Send notification that a tool is being called"""
        await self.websocket_manager.send_packet(
            UnifiedPacket(
                event=EventType.RESPONSE_FUNCTION_CALL,
                function_call={
                    "name": tool_call.name,
                    "arguments": tool_call.arguments
                }
            )
        )
    
    async def _send_tool_result_notification(self, tool_call: ToolCall) -> None:
        """Send notification of tool execution result"""
        await self.websocket_manager.send_packet(
            UnifiedPacket(
                event=EventType.RESPONSE_FUNCTION_CALL_RESULT,
                function_call={
                    "name": tool_call.name,
                    "output": {"success": True, "result": f"Executed {tool_call.name}"}
                }
            )
        )
    
    async def _handle_special_tool_behaviors(self, tool_call: ToolCall) -> None:
        """Handle special behaviors for specific tools"""
        # Handle SvcCopilotTmpl_ tools with topic logging
        if tool_call.name.startswith("SvcCopilotTmpl_"):
            topic = tool_call.name.split("__")[-1]
            await self.websocket_manager.send_packet(
                UnifiedPacket(
                    event=EventType.BENCHFORCE_LOG_TOPIC,
                    topic=topic
                )
            )
            logger.debug(f"Logged topic: {topic}")
