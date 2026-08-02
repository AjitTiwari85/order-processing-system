import json
import aio_pika

from app.config import settings
from app.core.logger import logger


async def publish_order_created(order):

    try:
        connection = await aio_pika.connect_robust(
            settings.RABBITMQ_URL
        )

        async with connection:

            channel = await connection.channel()

            await channel.declare_queue(
                "order.created",
                durable=True,
            )

            message = {
                "id": order.id,
                "customer_name": order.customer_name,
                "product_name": order.product_name,
                "quantity": order.quantity,
                "status": order.status,
            }

            await channel.default_exchange.publish(
                aio_pika.Message(
                    body=json.dumps(message).encode(),
                    delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
                ),
                routing_key="order.created",
            )

            logger.info(
                f"Published order.created event | Order ID: {order.id}"
            )

    except Exception as e:
        logger.error(
            f"Failed to publish order.created event | Error: {e}"
        )
        raise