import asyncio
import logging
import uuid
import traceback

from src.environments import configs
from src.classes.server import run_server_async
from src.metrics import metrics
from src.classes.evaluator import Evaluator
from src.classes.participants import ClientParticipant, AgentParticipant
from dotenv import load_dotenv
from tqdm import tqdm 

load_dotenv()


class Runner:
    def __init__(self, config):
        self.config = config
        self.environment = configs.get(config.environment)

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

    async def exec_entry(self, entry):
        base_session_id = f"{self.config.environment}.{entry.get('id')}.{str(uuid.uuid4())}"
        logging.info(f"Entry with id={base_session_id} started")

        tasks = []
        for i in range(1, self.config.task_iterations + 1):
            session_id = f"{base_session_id}-{i}"
            client_participant = ClientParticipant(
                session_id=session_id,
                entry=entry,
                config=self.config,
                environment=self.environment,
                evaluator=self.evaluator,
            )
            agent_participant = AgentParticipant(
                session_id=session_id,
                entry=entry,
                config=self.config,
                environment=self.environment,
            )
            tasks.append(
                asyncio.gather(
                    client_participant.create(),
                    agent_participant.create(),
                    return_exceptions=True  
                )
            )
        results = await asyncio.gather(*tasks)

        for task_result in results:
            for result in task_result:
                if isinstance(result, Exception):
                    logging.error("Exception occurred during participant creation:")
                    logging.error(''.join(traceback.format_exception(type(result), result, result.__traceback__)))

    async def start(self):
        logging.info("Starting Runner")
        
        server_task = asyncio.create_task(run_server_async(self.config.sample_rate))
        semaphore = asyncio.Semaphore(self.num_threads)

        async def sem_task(entry):
            async with semaphore:
                await self.exec_entry(entry)

        all_entries = self.environment.get("entries", [])
        if self.entries == [-1]:
            selected_entries = all_entries
        else:
            selected_entries = [all_entries[i] for i in self.entries if 0 <= i < len(all_entries)]

        tasks = [asyncio.create_task(sem_task(entry)) for entry in selected_entries]

        for future in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Processing entries"):
            await future

        server_task.cancel()
        try:
            await server_task
        except asyncio.CancelledError:
            logging.info("Server task cancelled, shutting down Runner.")

        logging.info("All conversations finished. Exiting.")

        final_results_df = self.evaluator.final_results()
        final_results_str = final_results_df.to_string(index=False)

        tqdm.write(f"\nEvaluation results:\n{final_results_str}")

