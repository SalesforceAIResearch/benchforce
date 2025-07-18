import asyncio
from threading import Event
import uuid
import json
import os
import websockets
import aiohttp
import datetime
import getpass
import platform
import aiofiles

from src.environments import configs
from src.classes.server import run_server_async
from src.classes.helper import Helper
from src.metrics import metrics
from src.classes.evaluator import Evaluator
from src.classes.participants import ClientParticipant, AgentParticipant
from src.classes import utils
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

logger = utils.make_logger(name="runner")


def new_runner_id():
    return str(uuid.uuid4())


def get_session_id(runner_id: str, entry_num: int, iteration_num: int):
    return f"{runner_id}.{entry_num:03d}.{iteration_num:02d}"


def parse_session_id(session_id: str):
    runner_id, entry_num, iteration_num = session_id.split(".")
    return runner_id, int(entry_num), int(iteration_num)


class Runner:
    def __init__(self, config, runner_id: str = None, with_agent = True, client_ready_event: Event = None, ws_host: str = "localhost", ws_port: int = 6789):
        self.config = config
        self.with_agent = with_agent
        self.environment = configs.get(config.environment)
        self.client_ready_event = client_ready_event

        self.ws_host = ws_host
        self.ws_port = ws_port

        if self.config.metrics == ['all']:
            self.metrics = metrics
        else:
            selected_keys = self.config.metrics
            self.metrics = {k: v for k, v in metrics.items() if k in selected_keys}
            invalid_keys = [k for k in selected_keys if k not in metrics]
            if invalid_keys:
                raise ValueError(f"Invalid metric keys: {invalid_keys}")

        self.evaluator = Evaluator(metrics=self.metrics)
        self.agent_mode = self.config.agent_mode
        self.client_mode = self.config.client_mode
        self.client_realtime_model = self.config.client_realtime_model
        self.agent_realtime_model = self.config.agent_realtime_model
        self.entries = self.config.entries
        self.num_threads = self.config.num_threads
        self.max_turns = self.config.max_turns
        self.runner_id = runner_id or new_runner_id()

        os.makedirs(Helper.get_run_base_path(runner_id=self.runner_id), exist_ok=True)
        self.results_file_path = Helper.get_run_result_file_path(runner_id=self.runner_id)

        self.ws: websockets.WebSocketClientProtocol | None = None

    async def connect_runner(self):
        uri = f"ws://{self.ws_host}:{self.ws_port}"
        logger.debug(f"connect_runner websockets.connect {uri}")
        self.ws = await websockets.connect(
            uri=uri,
            max_size=100 * 1024 * 1024,
            ping_interval=1,
            open_timeout=None,
            ping_timeout=None,
            close_timeout=None,
        )
        init_msg = {
            "session_id": self.runner_id,
            "role": "runner",
            "message": json.dumps({})
        }
        logger.debug("connect_runner ws.send")
        await self.ws.send(json.dumps(init_msg))

    async def send_final_results(self, json_results):
        if not self.ws:
            return
        final_payload = {
            "session_id": self.runner_id,
            "role": "runner",
            "message": json.dumps({
                "event": "runner.final_results",
                "data": json_results
            })
        }
        logger.debug("send_final_results ws.send")
        await self.ws.send(json.dumps(final_payload))

    async def exec_entry(self, entry):
        tasks = []
        for iteration_num in range(1, self.config.task_iterations + 1):
            session_id = get_session_id(
                runner_id=self.runner_id,
                entry_num=entry["entry_num"],
                iteration_num=iteration_num,
            )
            logger.debug(f"Executing: {session_id}")

            if self.ws:
                init_payload = {
                    "session_id": self.runner_id,
                    "role": "runner",
                    "message": json.dumps({
                        "event": "runner.entry_started",
                        "data": session_id
                    })
                }

                logger.debug("exec_entry ws.send")
                await self.ws.send(json.dumps(init_payload))
            
            logger.debug("instantiate client participant")
            client_participant = ClientParticipant(
                session_id=session_id,
                entry=entry,
                config=self.config,
                environment=self.environment,
                evaluator=self.evaluator,
                with_agent=self.with_agent,
                client_ready_event=self.client_ready_event,
                ws_host=self.ws_host,
                ws_port=self.ws_port,
            )

            logger.debug("create client participant")
            participant_tasks = [client_participant.create()]

            if self.with_agent:
                logger.debug("instantiate agent participant")
                agent_participant = AgentParticipant(
                    session_id=session_id,
                    entry=entry,
                    config=self.config,
                    environment=self.environment,
                    ws_host=self.ws_host,
                    ws_port=self.ws_port,
                )
                logger.debug("create agent participant")
                participant_tasks.append(agent_participant.create())

            logger.debug("gathering all participant tasks")
            tasks.append(
                asyncio.gather(*participant_tasks, return_exceptions=True)
            )

        logger.debug("exec_entry asyncio.gather")
        results = await asyncio.gather(*tasks, return_exceptions=True)  # Added return_exceptions=True
        logger.debug(f"exec_entry gathered {len(results)} results")

        for task_result in results:
            logger.debug("for task_result in results")
            for result in task_result:
                logger.debug("for result in task_result")
                if isinstance(result, Exception):
                    logger.error("Exception occurred during participant creation:")
                    logger.exception(result)

    async def start(self, with_server = True, show_progress = True):
        logger.info("Starting Runner")

        all_entries = self.environment.get("entries", [])

        if self.entries == [-1]:
            selected_entries = all_entries
        else:
            selected_entries = [all_entries[i] for i in self.entries if 0 <= i < len(all_entries)]
        
        if with_server:
            server_task = asyncio.create_task(run_server_async(self.config.sample_rate))

        await self.connect_runner()

        semaphore = asyncio.Semaphore(self.num_threads if self.with_agent else len(all_entries))

        async def sem_task(entry):
            async with semaphore:
                await self.exec_entry(entry)

        tasks = [asyncio.create_task(sem_task(entry)) for entry in selected_entries]

        for future in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Processing entries", disable=not show_progress):
            await future

        if with_server:
            server_task.cancel()
        try:
            if with_server:
                await server_task
        except asyncio.CancelledError:
            logger.info("Server task cancelled, shutting down Runner.")

        logger.info("All conversations finished. Exiting.")

        final_results_df, json_results = self.evaluator.final_results()
        final_results_str = final_results_df.to_string(index=False)

        tqdm.write(f"\nEvaluation results:\n{final_results_str}")

        enhanced_results = {
            **json_results,
            "metadata": {
                "current_user": os.environ.get("HOST_USER", getpass.getuser()),
                "saved_at": datetime.datetime.utcnow().isoformat() + "Z",
                "saved_at_timestamp": int(datetime.datetime.utcnow().timestamp()),
                "platform": platform.system(),
                "python_version": platform.python_version(),
                "environment": self.config.environment,
                "entries": self.entries,
            }
        }

        with open(self.results_file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(enhanced_results, indent=2))

        await self.send_final_results(enhanced_results)

        await self.ws.close()
