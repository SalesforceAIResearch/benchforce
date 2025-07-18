from abc import ABC, abstractmethod
import argparse
import asyncio
import datetime
import getpass
import json
import multiprocessing as mp
import os
import platform
import socket
import textwrap
from threading import Event
import time

from src.classes.agents.core.coordinator import Coordinator
from src.classes.agents.impl.example import ExampleAgent
from src.classes.agents.impl.openai import OpenAIAgent
from src.classes.constants import AUDIO_SAMPLE_RATE
from src.classes.helper import Helper
from src.classes import parser
from src.classes import runner
from src.classes import server
from src.classes import utils
from src.environments import configs

WS_HOST = "127.0.0.1"

logger = utils.make_logger(name="run")

AgentsByType = {
    agent.AGENT_CONFIG.type: agent
    for agent in (
        ExampleAgent,
        OpenAIAgent,
    )
}



class AsyncProcess(mp.Process, ABC):
    """
    A Process base-class for running async functions.
    """
    def __init__(self, mp_mgr: mp.Manager, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._run_success_lock = mp_mgr.Lock()
        self._run_success = mp_mgr.Value('i', 0)  # 0 = fail, 1 = success
    
    def debug(self, msg, **kwargs):
        logger.debug(f"{self.__class__.__name__}: {msg}", **kwargs)

    def info(self, msg, **kwargs):
        logger.info(f"{self.__class__.__name__}: {msg}", **kwargs)

    def warning(self, msg, **kwargs):
        logger.warning(f"{self.__class__.__name__}: {msg}", **kwargs)

    def error(self, msg, **kwargs):
        logger.error(f"{self.__class__.__name__}: {msg}", **kwargs)

    def exception(self, msg, **kwargs):
        logger.exception(f"{self.__class__.__name__}: {msg}", **kwargs)

    def run_success(self):
        with self._run_success_lock:
            return self._run_success.value == 1

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.debug("exiting")
        try:
            if self.is_alive():
                self.terminate()
                self.join(timeout=15)
                if self.is_alive():
                    self.warning("Process did not end in time, killing")
                    self.kill()
        finally:
            self.debug("exited")

    def run(self):
        self.debug("started")
        try:
            asyncio.run(self.async_run())
            with self._run_success_lock:
                self.debug("setting run_success to 1")
                self._run_success.value = 1
        except KeyboardInterrupt as e:
            self.debug("run_exception")
            self.run_exception = e
        except Exception as e:
            self.exception(e)
            self.run_exception = e
        finally:
            self.debug("stopped")

    @abstractmethod
    async def async_run(self):
        """
        Processes are marked successful unless they raise an exception.
        """
        pass


class Sockets(AsyncProcess):
    def __init__(self, mp_mgr: mp.Manager):
        super().__init__(mp_mgr=mp_mgr)

        # For notifying other processes the port to connect to
        self._port = mp_mgr.Value('i', 0)
        self._port_event = mp_mgr.Event()
        self._port_lock = mp_mgr.Lock()

        self._session_complete_event = mp_mgr.Event()

    @staticmethod
    def _find_free_port():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))  # Find a free port
            return s.getsockname()[1]

    def _set_port(self, port: int):
        with self._port_lock:
            self._port.value = port
            if port == 0:
                self._port_event.clear()
            else:
                self._port_event.set()

    def _get_port(self):
        with self._port_lock:
            if self._port.value == 0:
                return None
            return self._port.value

    def await_port(self, timeout: float):
        if not self._port_event.wait(timeout=timeout):
            return None
        return self._get_port()

    def new_session(self):
        self._session_complete_event.clear()

    def await_session_complete(self, timeout: float):
        return self._session_complete_event.wait(timeout=timeout)

    async def async_run(self):
        self.debug("Starting server")

        while True:  # Loop until a free port is found
            try:
                port = Sockets._find_free_port()
                async with server.WebSocketServer(
                    host=WS_HOST,
                    port=port,
                    sample_rate=AUDIO_SAMPLE_RATE,
                    started_cb=lambda host, port: self._set_port(port),
                    session_complete_cb=lambda session_id: self._session_complete_event.set(),
                ):
                    self.debug("Shutting down")
                self.debug("Done serving")
                return  # Server found a port and served it successfully
            except IOError as e:
                if e.errno == 98:  # Address already in use
                    self.warning(f"IOError starting server: {e}")
                else:
                    raise
            finally:
                self._set_port(0)


class RunAgent(AsyncProcess):
    def __init__(
            self,
            mp_mgr: mp.Manager,
            ws_port: int,
            client_ready_event: Event,
            mode: str,
            agent_type: str = OpenAIAgent.AGENT_CONFIG.type,
            config = None,
    ):
        super().__init__(mp_mgr=mp_mgr)
        self.ws_port = ws_port
        self.client_ready_event = client_ready_event
        self.mode = mode
        self.agent_type = agent_type
        self.config = config

    async def async_run(self):
        async def await_session_id():
            self.debug("Waiting for a session...")
            while True:
                try:
                    session_ids = await OpenAIAgent.get_pending_sessions(
                        host=WS_HOST,
                        port=self.ws_port,
                    )
                    if session_ids:
                        break
                except KeyboardInterrupt:
                    self.info("Keyboard interrupt")
                    return None
                except Exception as e:
                    self.warning(f"Error getting sessions: {e}")

                time.sleep(0.1)

            if len(session_ids) > 1:
                raise ValueError(f"Multiple sessions available: {session_ids}")

            session_id = session_ids[0]
            self.debug(f"Found a session! {session_id=}")
            return session_id

        self.debug("await_session_id")
        session_id = await await_session_id()
        if session_id is None:
            return

        self.debug(f"Creating {self.agent_type} agent")
        coordinator = Coordinator(
            agent=AgentsByType[self.agent_type](
                session_id=session_id,
                config_name="core",
                planner_env="local",
                mode=self.mode,
                config=self.config,
            ),
            config=self.config,
        )

        # The client must send its initial greeting before the agent can connect
        self.debug("Waiting for the client to report readiness...")
        while True:
            if self.client_ready_event.wait(timeout=0.1):
                self.debug("Client is ready!")
                break

        try:
            self.debug("agent.start")
            await coordinator.start(
                host=WS_HOST,
                port=self.ws_port,
            )
            self.debug("agent.start completed")
        finally:
            self.debug("agent.close")
            await coordinator.close()


class RunClient(AsyncProcess):
    def __init__(
            self,
            mp_mgr: mp.Manager,
            runner_id: str,
            entry_num: int,
            ws_port: int,
            client_ready_event: Event,
    ):
        super().__init__(mp_mgr=mp_mgr)
        self.runner_id = runner_id
        self.entry_num = entry_num
        self.ws_port = ws_port
        self.client_ready_event = client_ready_event

    async def async_run(self):
        entry_i = self.entry_num - 1  # 1-based to 0-based

        config = parser.parse()
        config.entries = [entry_i]
        self.debug(f"{config.entries=}")

        client = runner.Runner(
            runner_id=self.runner_id,
            config=config,
            with_agent=False,
            client_ready_event=self.client_ready_event,
            ws_host=WS_HOST,
            ws_port=self.ws_port,
        )

        entry = client.environment["entries"][entry_i]
        self.debug(f"""{entry["entry_num"]=} {entry["instructions"]=}""")

        self.debug("client.connect_runner")
        await client.connect_runner()

        self.debug("client.exec_entry")
        await client.exec_entry(entry=entry)

        self.debug("client.send_final_results")
        await client.send_final_results(json_results={})  # Actual results are computed later

        self.debug("client.ws.close")
        await client.ws.close()


class CompletionMarker:
    """
    A context manager that optionally marks a session as complete when it exits.
    Completion is marked by creating a COMPLETED file in the session directory.
    """
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.path = Helper.get_completed_file_path(session_id=session_id)
        self.is_complete = False
        self.start_time = None

    def set_complete(self, is_complete: bool):
        logger.debug(f"Set complete: {is_complete}")
        self.is_complete = is_complete

    def __enter__(self):
        try:
            os.remove(self.path)
        except FileNotFoundError:
            pass  # Never completed before

        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            return
        end_time = time.time()

        if self.is_complete:
            logger.info(f"✅ Session completed in {end_time - self.start_time:.2f}s")
            with open(self.path, "w") as f:
                f.write(self.session_id + "\n" + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        else:
            logger.info(f"❌ Session failed in {end_time - self.start_time:.2f}s")


def compute_result(runner_id: str, skip_upload: bool, run_iter: int, results_save_path=""):
    """
    A hacked-up copy of Runner.start()'s post-exec_entry metrics section
    """
    session_base_path = Helper.get_sessions_base_path()
    session_ids = []
    entry_nums = []
    with os.scandir(session_base_path) as it:
        for entry in it:
            if not entry.is_dir():
                continue
            if not entry.name.startswith(runner_id):
                continue

            session_ids.append(entry.name)
            _, entry_num, _ = runner.parse_session_id(entry.name)
            entry_nums.append(entry_num)

    session_ids.sort()
    entry_nums.sort()
    logger.info(f"Found {len(session_ids)} sessions: {entry_nums=}")

    config = parser.parse()
    config.entries = [entry_num - 1 for entry_num in entry_nums]  # 1-based to 0-based

    client = runner.Runner(
        runner_id=runner_id,
        config=config,
        with_agent=False,
        client_ready_event=None,
    )

    for session_id in session_ids:
        logger.info(f"Evaluating {session_id}...")
        file_path = Helper.get_transcript_file_path(session_id)
        if not os.path.exists(file_path):
            logger.warning(f"Transcript file not found for session {session_id}, skipping evaluation")
            continue
        _, entry_num, _ = runner.parse_session_id(session_id)
        entry_i = entry_num - 1
        entry = client.environment["entries"][entry_i]
        client.evaluator.check_entry(session_id, entry, client.environment)

    final_results_df, json_results = client.evaluator.final_results()
    final_results_str = final_results_df.to_string(index=False)
    lines = ["Evaluation results:"] + final_results_str.split("\n")
    print_box(lines)

    utcnow = datetime.datetime.now(datetime.UTC)
    enhanced_results = {
        **json_results,
        "metadata": {
            "current_user": os.environ.get("HOST_USER", getpass.getuser()),
            "saved_at": utcnow.isoformat() + "Z",
            "saved_at_timestamp": int(utcnow.timestamp()),
            "platform": platform.system(),
            "python_version": platform.python_version(),
            "environment": client.config.environment,
            "entries": client.entries,
            "config_metadata": getattr(client.config, "dashboard_export_meta", {}),
        }
    }

    if results_save_path:
        os.makedirs(results_save_path, exist_ok=True)
        with open(os.path.join(results_save_path, f'results_{run_iter}.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(enhanced_results, indent=2))
    else:
        with open(client.results_file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(enhanced_results, indent=2))


def print_box(lines: str | list[str], bold: bool = False, max_width: int = 76):
    if isinstance(lines, str):
        lines = [lines]
    max_len = min(max_width, max(len(line) for line in lines))

    def _gen_lines():
        for line in lines:
            yield from textwrap.wrap(line, width=max_len)

    ul, ur, ll, lr, h, v = "╔╗╚╝═║" if bold else "┌┐└┘─│"
    box = [ul + h * (max_len + 2) + ur]
    box.extend([
        v + " " + line + " " * (max_len - len(line)) + " " + v
        for line in _gen_lines()
    ])
    box.append(ll + h * (max_len + 2) + lr)
    logger.info("\n" + "\n".join(box))


def run(
        runner_id: str,
        entry_nums: list[int],
        skip_results: bool,
        skip_upload: bool,
        rerun_all: bool,
        mode: str,
        agent_type: str = "openai",
        config = None,
        run_iter=1,
):
    with (
        mp.Manager() as mp_mgr,
        Sockets(mp_mgr=mp_mgr) as ws,
    ):
        ws_port = ws.await_port(timeout=15)
        if ws_port is None:
            raise ValueError("Timed out waiting for the WebSocket server")
        logger.debug(f"Using WebSocket port {ws_port}")

        for entry_num in entry_nums:
            ws.new_session()
            session_id = runner.get_session_id(runner_id=runner_id, entry_num=entry_num, iteration_num=1)

            # Skip session if already completed
            if not rerun_all and Helper.is_session_completed(session_id=session_id, mode=mode):
                logger.info(f"Skipping completed {session_id}")
                continue

            # Run the session
            print_box("session_id: " + session_id)
            Helper.deleted_session_outputs(session_id=session_id)  # Clean up existing files
            with CompletionMarker(session_id=session_id) as cm:
                client_ready_event = mp_mgr.Event()
                with RunAgent(
                    mp_mgr=mp_mgr,
                    ws_port=ws_port,
                    client_ready_event=client_ready_event,
                    mode=mode,
                    agent_type=agent_type,
                    config=config,
                ) as agent:
                    with RunClient(
                        mp_mgr=mp_mgr,
                        runner_id=runner_id,
                        entry_num=entry_num,
                        ws_port=ws_port,
                        client_ready_event=client_ready_event,
                    ) as client:
                        while True:
                            client.join(timeout=0.1)

                            # See if client or agent decided to end the conversation
                            if not client.is_alive():
                                logger.info("📵 Client disconnected")
                                break
                            if not agent.is_alive():
                                logger.info("📵 Agent disconnected")
                                break

                        # On success, one participant will exit its run() method cleanly. The other will still be running.
                        cm.set_complete(client.run_success() or agent.run_success())

                # Give time for file writing to complete before terminating processes
                logger.info("⏳ Waiting for session to complete...")
                if not ws.await_session_complete(timeout=60):
                    raise TimeoutError("WebSocket server did not report session completion in time")

    logger.info(f"🎉 Done running all sessions")

    if not skip_results:
        logger.info("📝 Computing results...")
        compute_result(runner_id=runner_id, skip_upload=skip_upload, run_iter=run_iter, results_save_path=config.results_save_path)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--entry_nums", type=int, default=None, nargs="+", help="1-based entry numbers to run")
    p.add_argument("--runner_id", type=str, default=None, help="Optionally reuse an existing runner_id")

    p.add_argument("--skip_results", action="store_true", help="Skip computing results")
    p.add_argument("--skip_upload", action="store_true", help="Skip uploading computed results")
    p.add_argument("--run_iter", type=int, default=1, help="Number of times to run each session")

    p.add_argument("--results_only", action="store_true", help="Compute results on all cached sessions for a runner_id (accepts --skip_upload).")

    p.add_argument("--rerun_all", action="store_true", help="Rerun all sessions rather than only those missing outputs.")
    
    # Provider-related arguments
    p.add_argument("--agent", type=str, default= "openai", help="Agent provider to use (default: openai)")
    p.add_argument("--list_agents", action="store_true", help="List all available agents and exit")

    args = p.parse_args()

    # Handle provider listing
    if args.list_agents:
        lines = ["Available Agents:"]
        for agent_type, agent in AgentsByType.items():
            cfg = agent.AGENT_CONFIG
            lines.append(f"\"{agent_type}\"")
            lines.append(f"  Description: {cfg.description}")
            lines.append(f"  Voice support: {'Yes' if cfg.supports_voice else 'No'}")
            lines.append(f"  Text support: {'Yes' if cfg.supports_text else 'No'}")
            lines.append("")
        print_box(lines, bold=True)
        return

    lines = []

    config = parser.parse()

    skip_upload = args.skip_upload
    rerun_all = args.rerun_all
    agent_type = args.agent

    if args.runner_id:
        if not os.path.isdir(Helper.get_run_base_path(runner_id=args.runner_id)):
            raise FileNotFoundError(f"Runner_id specified does not exist locally: {args.runner_id}")

    if args.results_only:
        assert args.runner_id is not None, "Must provide a --runner_id with --results_only"
        lines.append(f"Computing results for {args.runner_id}")
        if skip_upload:
            lines.append("Skipping results upload")
        print_box(lines, bold=True)
        compute_result(runner_id=args.runner_id, skip_upload=skip_upload, run_iter=args.run_iter)
        return

    if not args.runner_id:
        runner_id = runner.new_runner_id()
        lines.append(f"NEW runner_id: {runner_id}")
    else:
        runner_id = args.runner_id
        lines.append(f"OLD runner_id: {runner_id}")

    lines.append("")
    lines.append(f"Agent: {agent_type}")

    if args.entry_nums is None:
        if not config.entries or -1 in config.entries:
            env = configs[config.environment]
            entry_nums = [i + 1 for i in range(len(env["entries"]))]
        else:
            entry_nums = [i + 1 for i in config.entries if i >= 0]  # 0-based to 1-based
        lines.append(f"config.yaml entries (1-based): {entry_nums}")
    else:
        entry_nums = args.entry_nums
        lines.append(f"arg entries (1-based): {entry_nums}")

    skip_results = args.skip_results
    if skip_results:
        lines.append("Skipping results computation")
    if skip_upload:
        lines.append("Skipping results upload")

    print_box(lines=lines, bold=True)

    run(
        runner_id=runner_id,
        entry_nums=entry_nums,
        skip_results=skip_results,
        skip_upload=skip_upload,
        rerun_all=rerun_all,
        mode=config.agent_mode,
        agent_type=agent_type,
        config=config,
        run_iter=args.run_iter,
    )

if __name__ == "__main__":
    main()

