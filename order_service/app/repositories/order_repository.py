from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Order
from app.schemas import OrderCreate


async def create_order(db: AsyncSession, order: OrderCreate):

    new_order = Order(
        customer_name=order.customer_name,
        product_name=order.product_name,
        quantity=order.quantity,
    )

    db.add(new_order)

    await db.commit()

    await db.refresh(new_order)

    return new_order