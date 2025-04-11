import asyncio
from src.classes.parser import parse
from src.classes.runner import Runner

async def main():
    try:
        config = parse()
        runner = Runner(config)
        await runner.start()
    except asyncio.CancelledError:
        print("Task was cancelled, shutting down...")
    except KeyboardInterrupt:
        print("KeyboardInterrupt detected, shutting down...")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program terminated by user.")