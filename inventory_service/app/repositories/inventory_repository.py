from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Inventory


async def get_product(
    db: AsyncSession,
    product_name: str,
):

    result = await db.execute(
        select(Inventory).where(
            Inventory.product_name == product_name
        )
    )

    return result.scalar_one_or_none()


async def update_stock(
    db: AsyncSession,
    product: Inventory,
    quantity: int,
):

    product.stock -= quantity

    await db.commit()

    await db.refresh(product)

    return product