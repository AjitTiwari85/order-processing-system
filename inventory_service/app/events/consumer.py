import json
import aio_pika

from app.core.config import settings
from app.db.session import AsyncSessionLocal
from app.services.inventory_service import process_order


async def process_message(
    message: aio_pika.IncomingMessage,
):

    async with message.process():

        order = json.loads(
            message.body.decode()
        )

        print("\nOrder Received")
        print(order)

        async with AsyncSessionLocal() as db:

            await process_order(
                db,
                order,
            )


async def start_consumer():

    connection = await aio_pika.connect_robust(
        settings.RABBITMQ_URL
    )

    channel = await connection.channel()

    queue = await channel.declare_queue(
        "order.created",
        durable=True,
    )

    await queue.consume(process_message)

    print("Inventory Consumer Started")

    return connection