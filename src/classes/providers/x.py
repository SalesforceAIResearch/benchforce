import os
import json
import logging
import asyncio

from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletionMessage

from src.classes.packet import UnifiedPacket, EventType
from src.classes.helper import Helper

class XAIText:
    def __init__(self, modalities, instructions, functions, functions_handler, base_model, agent_instance):
        self.client = OpenAI(api_key=os.environ.get("XAI_API_KEY"), base_url="https://api.x.ai/v1")
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

    async def process_client_messages(self, packet: UnifiedPacket):
        try:
            if packet.event == EventType.RESPONSE_TEXT_DONE:
                self.chat_context.append({"role": "user", "content": packet.text})
                await self.process_response_recursive(accumulated_tokens=0)
        except Exception as e:
            logging.error(f"Error in process_client_messages: {e}")
            error_packet = UnifiedPacket(
                event=EventType.RESPONSE_ERROR,
                error=str(e)
            )
            await self.agent_instance.produce(error_packet)
            await self.agent_instance.participant.terminate_session()
            await self.agent_instance.participant.handle_session_termination()

    async def process_response_recursive(self, accumulated_tokens=0):
        response = await asyncio.to_thread(
            self.client.chat.completions.create,
            model=self.base_model,
            messages=self.chat_context,
            tools=self.functions_arg,
            temperature=0.6
        )
        message: ChatCompletionMessage = response.choices[0].message
        total_tokens = accumulated_tokens + (response.usage.total_tokens or 0)
        
        if message.tool_calls:
            self.chat_context.append(message)
            for tool_call in message.tool_calls:
                function_name = tool_call.function.name
                try:
                    arguments = json.loads(tool_call.function.arguments)
                except Exception as e:
                    arguments = {}
                    logging.error(f"Error parsing arguments for function {function_name}: {e}")

                packet_func_call = UnifiedPacket(
                    event=EventType.RESPONSE_FUNCTION_CALL,
                    function_call={"name": function_name, "arguments": arguments}
                )
                await self.agent_instance.produce(packet_func_call)

                if function_name in self.functions:
                    result = await self.functions_handler(function_name, **arguments)
                else:
                    result = f"Error: Function {function_name} not found."

                packet_func_call_result = UnifiedPacket(
                    event=EventType.RESPONSE_FUNCTION_CALL_RESULT,
                    function_call={"name": function_name, "output": result}
                )
                await self.agent_instance.produce(packet_func_call_result)

                self.chat_context.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                })

            await self.process_response_recursive(accumulated_tokens=total_tokens)
        else:
            self.chat_context.append(message)
            packet_text = UnifiedPacket(
                event=EventType.RESPONSE_TEXT_DONE,
                text=message.content,
                tokens=total_tokens
            )
            await self.agent_instance.produce(packet_text)
            done_packet = UnifiedPacket(event=EventType.RESPONSE_DONE)
            await self.agent_instance.produce(done_packet)

