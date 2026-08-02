import json
import asyncio
import aio_pika

from app.core.config import settings
from app.core.logger import logger
from app.services.notification_service import (
    send_confirmation_email,
    send_rejection_email,
)


async def process_confirm(message: aio_pika.IncomingMessage):

    async with message.process():

        data = json.loads(message.body.decode())

        logger.info(
            f"Received order.confirmed event | Order ID: {data['id']}"
        )

        asyncio.create_task(
            send_confirmation_email(data)
        )


async def process_reject(message: aio_pika.IncomingMessage):

    async with message.process():

        data = json.loads(message.body.decode())

        logger.warning(
            f"Received order.rejected event | Order ID: {data['id']}"
        )

        asyncio.create_task(
            send_rejection_email(data)
        )


async def start_consumer():

    try:
        connection = await aio_pika.connect_robust(
            settings.RABBITMQ_URL
        )

        channel = await connection.channel()

        confirmed_queue = await channel.declare_queue(
            "order.confirmed",
            durable=True,
        )

        rejected_queue = await channel.declare_queue(
            "order.rejected",
            durable=True,
        )

        await confirmed_queue.consume(process_confirm)
        await rejected_queue.consume(process_reject)

        logger.info("Notification Consumer Started Successfully")

        return connection

    except Exception as e:
        logger.error(f"Failed to start Notification Consumer: {e}")
        raise