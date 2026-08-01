import asyncio

from app.db.session import AsyncSessionLocal
from app.models import Inventory


async def seed():

    async with AsyncSessionLocal() as session:

        session.add_all(
            [
                Inventory(
                    product_name="Laptop",
                    stock=10
                ),
                Inventory(
                    product_name="Mouse",
                    stock=25
                ),
                Inventory(
                    product_name="Keyboard",
                    stock=15
                ),
            ]
        )

        await session.commit()

        print("Inventory Seeded")


asyncio.run(seed())