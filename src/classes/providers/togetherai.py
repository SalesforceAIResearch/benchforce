import os
import json
import logging
import asyncio

from together.types.chat_completions import ChatCompletionMessage
from together import Together

from src.classes.packet import UnifiedPacket, EventType
from src.classes.helper import Helper

class TogetherAIText:
    def __init__(self, modalities, instructions, functions, functions_handler, base_model, agent_instance):
        self.client = Together(api_key=os.environ.get("TOGETHERAI_API_KEY"))
        self.modalities = modalities
        self.base_model = base_model
        self.instructions = instructions
        self.functions = functions
        self.functions_handler = functions_handler
        self.agent_instance = agent_instance
        self.agent_instance.set_consumer(self.process_client_messages)
        self.chat_context = [
            {"role": "system", "content": self.instructions}
        ]
        self.parsed_functions = Helper.xai_parse_functions(list(self.functions.values()))
        self.functions_arg = self.parsed_functions if self.parsed_functions else None


    async def connect(self):
        if self.agent_instance.participant.type == "client":

            response = await asyncio.to_thread(
                self.client.chat.completions.create,
                model=self.base_model,
                messages=[*self.chat_context, {"role": "user", "content": "Start conversation with appropriate first message according to your instructions"}],
                temperature=0.6
            )

            message: ChatCompletionMessage = response.choices[0].message
            packet_text = UnifiedPacket(
                event=EventType.RESPONSE_TEXT_DONE,
                text=message.content,
                tokens=response.usage.total_tokens
            )
            await self.agent_instance.produce(packet_text)

    async def process_model_events(self):     
        pass

    async def process_client_messages(self, packet: UnifiedPacket):
        try:
            if packet.event == EventType.RESPONSE_TEXT_DONE:
                self.chat_context.append({"role": "user", "content": f"{packet.text}"})
                response = await asyncio.to_thread(
                    self.client.chat.completions.create,
                    model=self.base_model,
                    messages=self.chat_context,
                    tools=self.functions_arg,
                    temperature=0.6
                )

                message: ChatCompletionMessage = response.choices[0].message
                if message.tool_calls:

                    tool_calls = []
                    tool_calls.append(message) 

                    for tool_call in response.choices[0].message.tool_calls:

                        function_name = tool_call.function.name
                        arguments = json.loads(tool_call.function.arguments)

                        packet_func_call = UnifiedPacket(
                            event=EventType.RESPONSE_FUNCTION_CALL,
                            function_call={"name": function_name, "arguments": arguments}
                        )
                        await self.agent_instance.produce(packet_func_call)

                        if function_name in self.functions:
                            result = await self.functions_handler(function_name, **arguments)
                        else:
                            result = f"Error: Function {function_name} not found."

                        tool_calls.append({
                            "name": function_name,
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": str(result)
                        })

                        packet = UnifiedPacket(
                            event=EventType.RESPONSE_FUNCTION_CALL_RESULT, 
                            function_call={
                                "name": function_name,
                                "output": result
                            }
                        )

                        await self.agent_instance.produce(packet)

                    self.chat_context.extend(tool_calls) 

                    final_response = await asyncio.to_thread(
                        self.client.chat.completions.create,
                        model=self.base_model,
                        messages=self.chat_context,
                        tools=self.functions_arg,
                        temperature=0.6
                    )
                    final_message: ChatCompletionMessage = final_response.choices[0].message
                    self.chat_context.append(final_message)

                    packet_text = UnifiedPacket(
                        event=EventType.RESPONSE_TEXT_DONE,
                        text=final_message.content,
                        tokens = (response.usage.total_tokens or 0) + (final_response.usage.total_tokens or 0)
                    )
                    await self.agent_instance.produce(packet_text)
                else:
                    self.chat_context.append(message)
                    packet_text = UnifiedPacket(
                        event=EventType.RESPONSE_TEXT_DONE,
                        text=message.content,
                        tokens=response.usage.total_tokens
                    )
                    await self.agent_instance.produce(packet_text)
                
                done_packet = UnifiedPacket(event=EventType.RESPONSE_DONE)
                await self.agent_instance.produce(done_packet)

        except Exception as e:
            logging.error(f"Error in process_client_messages: {e}")
            error_packet = UnifiedPacket(
                event=EventType.RESPONSE_ERROR,
                error=str(e)
            )
            await self.agent_instance.produce(error_packet)
            await self.agent_instance.participant.terminate_session()
            await self.agent_instance.participant.handle_session_termination()

