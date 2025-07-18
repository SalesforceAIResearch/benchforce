import os
import json
import logging
import base64
import asyncio
import websockets

from openai import AsyncOpenAI, OpenAI
from openai.types.chat.chat_completion import ChatCompletionMessage

from src.classes.packet import UnifiedPacket, EventType
from src.classes.helper import Helper


class OpenAIRealtime:
    def __init__(self, modalities, instructions, functions, functions_handler, base_model, agent_instance, voice):
        self.client = AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.modalities = ["audio", "text"] if modalities == ["audio"] else modalities
        self.base_model = base_model
        self.instructions = instructions
        self.functions = functions
        self.functions_handler = functions_handler
        self.agent_instance = agent_instance
        self.voice = voice
        self.agent_instance.set_consumer(self.process_client_messages)
        self.audio_buffer = bytearray()
        self.text_buffer = ""

    async def connect(self):
        async with self.client.beta.realtime.connect(
            model=self.base_model
        ) as connection:
            self.connection = connection
            await connection.session.update(
                session={
                    "modalities": self.modalities,
                    "input_audio_format": "pcm16",
                    "output_audio_format": "pcm16",
                    "turn_detection": None,
                    "voice": self.voice,
                    "instructions": self.instructions,
                    #"temperature": 0.6,
                    "temperature": 0,
                    "tools": Helper.oai_rt_parse_functions(list(self.functions.values())),
                    "tool_choice": "auto",
                }
            )
            livekit_api_agent = getattr(self.agent_instance, 'livekit_api_agent', False)

            if self.agent_instance.participant.type == "client" and not livekit_api_agent:

                await connection.conversation.item.create(
                    item={
                        "type": "message",
                        "role": "user",
                        "content": [{"type": "input_text", "text": "Start conversation with appropriate first message according to your instructions"}],
                    }
                )
                await connection.response.create()


            async for event in connection:
                await self.process_model_events(event)


    async def process_client_messages(self, packet: UnifiedPacket):
        try:
            if packet.event == EventType.RESPONSE_TEXT_DONE:
                await self.connection.conversation.item.create(
                    item={
                        "type": "message",
                        "role": "user",
                        "content": [
                            {
                                "type": "input_text",
                                "text": packet.text,
                            }
                        ],
                    }
                )

                await self.connection.response.create()

            elif packet.event == EventType.RESPONSE_AUDIO_DELTA:
                await self.connection.input_audio_buffer.append(audio=packet.audio_delta)

                if self.agent_instance.is_async:
                    await self.connection.input_audio_buffer.commit()

            elif packet.event == EventType.RESPONSE_AUDIO_DONE:

                await self.connection.input_audio_buffer.append(audio=packet.audio)
                await self.connection.input_audio_buffer.commit()
                await self.connection.response.create()


        except websockets.exceptions.ConnectionClosed:
            logging.info("Websocket connection with client closed")
        except Exception as e:
            logging.error(f"Error processing incoming message: {e}")
            error_packet = UnifiedPacket(
                event=EventType.RESPONSE_ERROR,
                error=str(e)
            )
            await self.agent_instance.produce(error_packet)
            await self.agent_instance.participant.terminate_session()
            await self.agent_instance.participant.handle_session_termination()

    async def process_model_events(self, event):
        try:
            if event.type == "response.audio.delta":
                if self.agent_instance.is_async:
                    packet = UnifiedPacket(
                        event=EventType.RESPONSE_AUDIO_DELTA, audio_delta=event.delta
                    )
                    await self.agent_instance.produce(packet)
                else:
                    self.audio_buffer.extend(base64.b64decode(event.delta))

            elif event.type == "response.audio.done":
                if self.agent_instance.is_async:
                    packet = UnifiedPacket(
                        event=EventType.RESPONSE_AUDIO_DONE,
                    )
                    await self.agent_instance.produce(packet)
                else:
                    if self.audio_buffer:
                        packet = UnifiedPacket(
                            event=EventType.RESPONSE_AUDIO_DONE,
                            audio=base64.b64encode(bytes(self.audio_buffer)).decode("utf-8"),
                        )
                        await self.agent_instance.produce(packet)
                        self.audio_buffer.clear()


            elif event.type == "response.audio_transcript.done":
                packet = UnifiedPacket(
                    event=EventType.RESPONSE_AUDIO_TRANSCRIPT_DONE,
                    text=event.transcript,
                )
                await self.agent_instance.produce(packet)

            elif event.type == "response.text.done":
                packet = UnifiedPacket(
                    event=EventType.RESPONSE_TEXT_DONE, text=event.text
                )
                await self.agent_instance.produce(packet)
                self.text_buffer = ""

            elif event.type == "response.text.delta":
                if self.agent_instance.is_async:
                    packet = UnifiedPacket(
                        event=EventType.RESPONSE_TEXT_DELTA, text_delta=event.delta
                    )
                    await self.agent_instance.produce(packet)
                else:
                    self.text_buffer += (" " + event.delta) if len(self.text_buffer) else event.delta

            elif event.type == "response.output_item.done" and event.item.type == "function_call":
                try:
                    function_name = event.item.name
                    arguments = json.loads(event.item.arguments)

                    packet = UnifiedPacket(
                        event=EventType.RESPONSE_FUNCTION_CALL,
                        function_call={
                            "name": event.item.name,
                            "arguments": arguments
                        }
                    )

                    await self.agent_instance.produce(packet)

                    if function_name in self.functions:
                        output = await self.functions_handler(function_name, **arguments)
                        await self.connection.conversation.item.create(
                            item={
                                "type": "function_call_output",
                                "call_id": event.item.call_id,
                                "output": output
                            }
                        )

                        packet = UnifiedPacket(
                            event=EventType.RESPONSE_FUNCTION_CALL_RESULT,
                            function_call={
                                "name": event.item.name,
                                "output": output
                            }
                        )

                        await self.agent_instance.produce(packet)
                        await self.connection.response.create()

                    else:
                        logging.error(f"Function {function_name} not found!")

                except Exception as e:
                    logging.error(f"Error executing function {function_name}: {e}")
                
            elif event.type == "error":
                packet = UnifiedPacket(
                    event=EventType.RESPONSE_ERROR, error=event.error
                )
                await self.agent_instance.produce(packet)

            elif event.type == "response.done":
                packet = UnifiedPacket(event=EventType.RESPONSE_DONE)
                await self.agent_instance.produce(packet)

        except Exception as e:
            logging.error(f"Error processing model event: {event.type} {e}")


class OpenAIText:
    def __init__(self, modalities, instructions, functions, functions_handler, base_model, agent_instance):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
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
        self.parsed_functions = Helper.oai_parse_functions(list(self.functions.values()))
        self.functions_arg = self.parsed_functions if self.parsed_functions else None

    async def connect(self):
        livekit_api_agent = getattr(self.agent_instance, 'livekit_api_agent', False)
        
        if self.agent_instance.participant.type == "client" and not livekit_api_agent:
            response = await asyncio.to_thread(
                self.client.chat.completions.create,
                model=self.base_model,
                messages=[*self.chat_context, {"role": "user", "content": "Start conversation with appropriate first message according to your instructions"}],
                #temperature=0.6
                temperature=0
                
            )
            message: ChatCompletionMessage = response.choices[0].message
            self.chat_context.append(message)

            packet_text = UnifiedPacket(
                event=EventType.RESPONSE_TEXT_DONE,
                text=message.content,
                tokens=response.usage.total_tokens
            )
            packet_done = UnifiedPacket(
                event=EventType.RESPONSE_DONE,
            )
            await self.agent_instance.produce(packet_text)
            await self.agent_instance.produce(packet_done)
            logging.info(f"Initial message sent successfully")
        else:
            logging.info(f"Skipping initial message")

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
            #temperature=0.6
            temperature=0
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
