import asyncio
import concurrent.futures
import logging
from temporalio.client import Client
from temporalio.worker import Worker
from workers.backend.activities.name import say_hello
from workers.backend.worker import GreetingWorkflow

logging.basicConfig(level=logging.INFO)

async def main():
    try:
        logging.info("Connecting to Temporal server...")
        client = await asyncio.wait_for(Client.connect('localhost:7233'), timeout=10)
        logging.info("Connected to Temporal server.")

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            worker = Worker(client, task_queue='name-task-queue', workflows=[GreetingWorkflow], activities=[say_hello], activity_executor=executor)
            logging.info("Starting worker...")
            await worker.run()
    except asyncio.TimeoutError:
        logging.error("Connection to Temporal server timed out.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    logging.info("Starting Temporal worker...")
    asyncio.run(main())