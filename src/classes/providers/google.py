import os
import json
import logging
import base64
import asyncio

from google import genai
from google.genai import types

from src.classes.packet import UnifiedPacket, EventType
from src.classes.helper import Helper
from src.classes.providers.deepgram import DeepgramSTT

class GoogleRealtime:
    def __init__(self, modalities, instructions, functions, functions_handler, base_model, agent_instance, voice=None):
        self.modalities = [m.upper() for m in modalities]
        self.instructions = instructions
        self.functions = functions
        self.functions_handler = functions_handler
        self.base_model = base_model
        self.agent_instance = agent_instance
        self.voice = voice
        self.stt = DeepgramSTT(self.agent_instance.participant.config.agent_stt_model)
        self.CHUNK = 24000

        self.parsed_functions = Helper.google_parse_functions(list(self.functions.values()))
        self.functions_arg = self.parsed_functions if self.parsed_functions else None
        tools = types.Tool(function_declarations=self.parsed_functions) if self.parsed_functions else None

        self.config = {
            "response_modalities": self.modalities, 
            "system_instruction": types.Content(
                parts=[
                    types.Part(
                        text=self.instructions
                    )
                ]
            ),
            "tools": [tools] if tools else None,
            "session_resumption": {
                "handle":"previous_session_handle"
            },
        }

        self.client = genai.Client(
            api_key=os.environ.get("GEMINI_API_KEY"),
            http_options={'api_version': 'v1alpha'}
        )

        self.audio_buffer = bytearray()
        self.text_buffer = ""

        self.agent_instance.set_consumer(self.process_client_messages)

    async def connect(self):
        async with self.client.aio.live.connect(model=self.base_model, config=self.config) as session:
            self.session = session

            if getattr(self.agent_instance.participant, "type", None) == "client":
                init_message = "Start conversation with appropriate first message according to your instructions"
                await session.send(input=init_message, end_of_turn=True)

            while not self.agent_instance.participant.terminated:
                async for response in self.session.receive():
                    if hasattr(response, "session_resumption_update") and response.session_resumption_update:
                        update = response.session_resumption_update
                        if update.resumable and update.new_handle:
                            return update.new_handle
            
                    await self.process_model_response(response)

    async def process_client_messages(self, packet):
        try:
            if packet.event == EventType.RESPONSE_TEXT_DONE:
                await self.session.send(input=packet.text, end_of_turn=True)

            elif packet.event == EventType.RESPONSE_AUDIO_DELTA:
                pass

            elif packet.event == EventType.RESPONSE_AUDIO_DONE:

                await self.session.send(input={"data": bytes(base64.b64decode(packet.audio)), "mime_type": "audio/pcm"}, end_of_turn=False)
                await self.session.send(input={"data": b"\x00" * 2 * self.CHUNK, "mime_type": "audio/pcm"}, end_of_turn=True)

        except Exception as e:
            logging.error(f"Error in process_client_messages: {e}")
            error_packet = UnifiedPacket(
                event=EventType.RESPONSE_ERROR,
                error=str(e)
            )
            await self.agent_instance.produce(error_packet)
            await self.agent_instance.participant.terminate_session()
            await self.agent_instance.participant.handle_session_termination()

    async def process_model_response(self, response):       
        try:
            if hasattr(response, "text") and response.text is not None:
                packet = UnifiedPacket(event=EventType.RESPONSE_TEXT_DONE, text=response.text)
                await self.agent_instance.produce(packet)
                self.text_buffer = ""

            if hasattr(response, "data") and response.data is not None:
                self.audio_buffer.extend(response.data)
   
            if hasattr(response, "tool_call") and response.tool_call is not None:
                tool_calls: types.LiveServerToolCall = response.tool_call
                for function_call in tool_calls.function_calls:
                    function_name = function_call.name
                    arguments = function_call.args
                    id = function_call.id

                    try:
                        if isinstance(arguments, str):
                            arguments = json.loads(arguments)
                    except Exception:
                        arguments = {}

                    packet = UnifiedPacket(
                        event=EventType.RESPONSE_FUNCTION_CALL,
                        function_call={"name": function_name, "arguments": arguments}
                    )

                    await self.agent_instance.produce(packet)

                    if function_name in self.functions:
                        output = await self.functions_handler(function_name, **arguments)
                        function_response=types.FunctionResponse(
                            name=function_name,
                            response={'result': json.loads(output)},
                            id=id,
                        )

                        await self.session.send(input={"function_responses":[function_response]}, end_of_turn=False)
                        await self.session.send(input={"data": b"\x00" * 2 * self.CHUNK, "mime_type": "audio/pcm"}, end_of_turn=False)

                        result_packet = UnifiedPacket(
                            event=EventType.RESPONSE_FUNCTION_CALL_RESULT,
                            function_call={"name": function_name, "output": output}
                        )
                        await self.agent_instance.produce(result_packet)
                    else:
                        logging.error(f"{function_name}")


            if hasattr(response, "error") and response.error is not None:
                packet = UnifiedPacket(event=EventType.RESPONSE_ERROR, error=response.error)
                await self.agent_instance.produce(packet)

            if hasattr(response, "done") and response.done:
                packet = UnifiedPacket(event=EventType.RESPONSE_DONE)
                await self.agent_instance.produce(packet)

            if hasattr(response, "server_content") and response.server_content is not None:
                if response.server_content.turn_complete: 
                    if self.audio_buffer:
                        packet = UnifiedPacket(
                            event=EventType.RESPONSE_AUDIO_DONE,
                            audio=base64.b64encode(bytes(self.audio_buffer)).decode("utf-8")
                        )

                        transcript = self.stt.process_audio(bytes(self.audio_buffer))

                        text_packet = UnifiedPacket(
                            event=EventType.RESPONSE_AUDIO_TRANSCRIPT_DONE,
                            text=transcript,
                        )
                        self.audio_buffer.clear()
                        await asyncio.sleep(2)
                        await self.agent_instance.produce(text_packet)
                        await self.agent_instance.produce(packet)


        except Exception as e:
            logging.error(f"{e}")
                


class GoogleText:
    def __init__(self, modalities, instructions, functions, functions_handler, base_model, agent_instance):
        self.client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
        self.modalities = modalities
        self.base_model = base_model
        self.instructions = instructions
        self.functions = functions
        self.functions_handler = functions_handler
        self.agent_instance = agent_instance
        self.agent_instance.set_consumer(self.process_client_messages)
        self.chat_context = []
        self.parsed_functions = Helper.google_parse_functions(list(self.functions.values()))
        self.functions_arg = self.parsed_functions if self.parsed_functions else None
        tools = types.Tool(function_declarations=self.parsed_functions) if self.parsed_functions else None
        self.config = types.GenerateContentConfig(
            tools=[tools] if tools else None, 
            system_instruction=[self.instructions]
        )
        

    async def connect(self):
        if self.agent_instance.participant.type == "client":

            response = await self.client.aio.models.generate_content(
                model=self.base_model,
                contents=[
                    types.Content(
                        role='user',
                        parts=[types.Part.from_text(text='Start conversation with appropriate first message according to your instructions')],
                    ),
                ],
                config=self.config,
            )
            message = response.text

            self.chat_context.append(
                types.Content(
                    role='user',
                    parts=[types.Part.from_text(text=message)],
                )
            )
            
            packet_text = UnifiedPacket(
                event=EventType.RESPONSE_TEXT_DONE,
                text=str(message)
            )
            await self.agent_instance.produce(packet_text)


    async def process_model_events(self):     
        pass

    async def process_client_messages(self, packet: UnifiedPacket):
        try:
            if packet.event == EventType.RESPONSE_TEXT_DONE:
                self.chat_context.append(
                    types.Content(
                        role='user',
                        parts=[types.Part.from_text(text=packet.text)],
                    )
                )
                
                response = await self.client.aio.models.generate_content(
                    model=self.base_model,
                    contents=self.chat_context,
                    config=self.config,
                )
                message = response.text
    
                for part in response.candidates[0].content.parts:
                    if part.function_call:
                        function_call = part.function_call

                        function_call_name = function_call.name
                        arguments = function_call.args

                        self.chat_context.append(types.Content(role="model", parts=[types.Part(function_call=function_call)]))

                        packet_func_call = UnifiedPacket(
                            event=EventType.RESPONSE_FUNCTION_CALL,
                            function_call={"name": function_call_name, "arguments": arguments}
                        )

                        await self.agent_instance.produce(packet_func_call)

                        try:
                            result = await self.functions_handler(function_call_name, **arguments)
                            
                            function_response = {'result': result}
                        except (
                            Exception
                        ) as e:
                            function_response = {'error': str(e)}

                        packet = UnifiedPacket(
                            event=EventType.RESPONSE_FUNCTION_CALL_RESULT, 
                            function_call={
                                "name": function_call_name,
                                "output": function_response
                            }
                        )

                        await self.agent_instance.produce(packet)

                        function_response_part = types.Part.from_function_response(
                            name=function_call_name,
                            response=function_response,
                        )

                        function_response_content = types.Content(
                            role='user', parts=[function_response_part]
                        )

                        self.chat_context.append(function_response_content)

                    final_response = await self.client.aio.models.generate_content(
                        model=self.base_model,
                        contents=self.chat_context,
                        config=self.config,
                    )

                    final_message = final_response.text
                    self.chat_context.append(
                        types.Content(
                            role='model',
                            parts=[types.Part.from_text(text=final_message)],
                        )
                    )

                    packet_text = UnifiedPacket(
                        event=EventType.RESPONSE_TEXT_DONE,
                        text=final_message,
                        tokens=response.usage_metadata.total_token_count + final_response.usage_metadata.total_token_count
                    )
                    await self.agent_instance.produce(packet_text)
                else:
                    self.chat_context.append(
                        types.Content(
                            role='model',
                            parts=[types.Part.from_text(text=message)],
                        )
                    )
                    packet_text = UnifiedPacket(
                        event=EventType.RESPONSE_TEXT_DONE,
                        text=message,
                        tokens=response.usage_metadata.total_token_count
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
    
