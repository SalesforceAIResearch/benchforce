import anthropic
import logging
import os

from anthropic.types.message import Message, ContentBlock
from anthropic.types import TextBlock
from typing import List

from src.classes.packet import UnifiedPacket, EventType
from src.classes.helper import Helper


class AnthropicText:
    def __init__(self, modalities, instructions, functions, functions_handler, base_model, agent_instance):
        self.client = anthropic.AsyncAnthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        self.modalities = modalities
        self.base_model = base_model
        self.instructions = instructions
        self.functions = functions
        self.functions_handler = functions_handler
        self.agent_instance = agent_instance
        self.agent_instance.set_consumer(self.process_client_messages)
        self.chat_context = []
        self.parsed_functions = Helper.anthropic_parse_functions(list(self.functions.values()))
        self.functions_arg = self.parsed_functions if self.parsed_functions else []

    async def connect(self):
        if self.agent_instance.participant.type == "client":

            response: Message = await self.client.messages.create(
                    max_tokens=1000,
                    model=self.base_model,
                    system=self.instructions,
                    temperature=0.6,
                    messages=[{"role": "user", "content": "Start conversation with appropriate first message according to your instructions"}],
            )

            message = response.content[0].text

            input_tokens = getattr(response.usage, "input_tokens", 0) or 0
            output_tokens = getattr(response.usage, "output_tokens", 0) or 0
            total_tokens = input_tokens + output_tokens

            self.chat_context.append({"role": "user", "content": message})
            packet_text = UnifiedPacket(
                event=EventType.RESPONSE_TEXT_DONE,
                text=str(message),
                tokens=total_tokens
            )
            await self.agent_instance.produce(packet_text)


    async def process_model_events(self):     
        pass

    async def process_client_messages(self, packet: UnifiedPacket):
        try:
            if packet.event == EventType.RESPONSE_TEXT_DONE:
                self.chat_context.append({"role": "user", "content": packet.text})
                response: Message = await self.client.messages.create(
                    max_tokens=1000,
                    model=self.base_model,
                    system=self.instructions,
                    temperature=0.6,
                    tools=self.functions_arg,
                    messages=self.chat_context,
                )
                
                input_tokens = getattr(response.usage, "input_tokens", 0) or 0
                output_tokens = getattr(response.usage, "output_tokens", 0) or 0
                total_tokens = input_tokens + output_tokens

                message: List[ContentBlock] = response.content
                if response.stop_reason == 'tool_use':

                    function_call = next(block for block in message if block.type == "tool_use")
                    function_name = function_call.name
                    arguments = function_call.input

                    packet_func_call = UnifiedPacket(
                        event=EventType.RESPONSE_FUNCTION_CALL,
                        function_call={"name": function_name, "arguments": arguments}
                    )
                    
                    await self.agent_instance.produce(packet_func_call)
                    
                    if function_name in self.functions:
                        result = await self.functions_handler(function_name, **arguments)
                        packet = UnifiedPacket(
                            event=EventType.RESPONSE_FUNCTION_CALL_RESULT, 
                            function_call={
                                "name": function_name,
                                "output": result
                            }
                        )
                        await self.agent_instance.produce(packet)
                    
                    else:
                        result = f"Error: Function {function_name} not found."

                    self.chat_context.append({"role": "assistant", "content": message}) 
                    self.chat_context.append({
                        "role": "user",
                        "content": [
                            {
                                "type": "tool_result",
                                "tool_use_id": function_call.id,
                                "content": str(result),
                            }
                        ]
                    })

                    final_response = await self.client.messages.create(
                        max_tokens=1000,
                        model=self.base_model,
                        system=self.instructions,
                        temperature=0.6,
                        tools=self.functions_arg,
                        messages=self.chat_context,
                    )
                    final_input_tokens = getattr(final_response.usage, "input_tokens", 0) or 0
                    final_output_tokens = getattr(final_response.usage, "output_tokens", 0) or 0
                    final_total_tokens = final_input_tokens + final_output_tokens

                    final_message = next(
                        (block.text for block in final_response.content if isinstance(block, TextBlock)),
                        None,
                    )

                    self.chat_context.append({"role": "assistant", "content": final_message})
                    packet_text = UnifiedPacket(
                        event=EventType.RESPONSE_TEXT_DONE,
                        text=str(final_message),
                        tokens=total_tokens + final_total_tokens
                    )
                    await self.agent_instance.produce(packet_text)
                else:
                    self.chat_context.append({"role": "assistant", "content": message[0].text})
                    packet_text = UnifiedPacket(
                        event=EventType.RESPONSE_TEXT_DONE,
                        text=str(message[0].text),
                        tokens=total_tokens
                    )
                    await self.agent_instance.produce(packet_text)
                
                done_packet = UnifiedPacket(event=EventType.RESPONSE_DONE)
                await self.agent_instance.produce(done_packet)

        except Exception as e:
            logging.error(self.chat_context)
            logging.error(f"Error in process_client_messages: {e}")
            error_packet = UnifiedPacket(
                event=EventType.RESPONSE_ERROR,
                error=str(e)
            )
            await self.agent_instance.produce(error_packet)
            await self.agent_instance.participant.terminate_session()
            await self.agent_instance.participant.handle_session_termination()