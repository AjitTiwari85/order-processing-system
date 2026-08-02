import json
import aio_pika
from app.core.logger import logger

from app.core.config import settings


async def publish_event(
    routing_key: str,
    message: dict,
):

    connection = await aio_pika.connect_robust(
        settings.RABBITMQ_URL
    )

    async with connection:

        channel = await connection.channel()

        await channel.declare_queue(
            routing_key,
            durable=True,
        )

        await channel.default_exchange.publish(

            aio_pika.Message(

                body=json.dumps(message).encode(),

                delivery_mode=aio_pika.DeliveryMode.PERSISTENT,

            ),

            routing_key=routing_key,

        )

        logger.info(f"Published -> {routing_key}")