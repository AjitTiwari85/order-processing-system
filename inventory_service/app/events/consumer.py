import json
import aio_pika

from app.core.config import settings


async def process_message(message: aio_pika.IncomingMessage):

    async with message.process():

        body = json.loads(message.body.decode())

        print()

        print("=" * 50)
        print("Order Received")
        print(body)
        print("=" * 50)
        print()


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

    print("Inventory Consumer Started...")

    return connection