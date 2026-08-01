import json
import aio_pika

RABBITMQ_URL = "amqp://guest:guest@localhost/"


async def publish_order_created(order):

    connection = await aio_pika.connect_robust(RABBITMQ_URL)

    async with connection:

        channel = await connection.channel()

        await channel.declare_queue(
            "order.created",
            durable=True
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

                delivery_mode=aio_pika.DeliveryMode.PERSISTENT

            ),

            routing_key="order.created"

        )

        print("Event Published :", message) 