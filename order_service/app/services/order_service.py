from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import OrderCreate

from app.repositories.order_repository import create_order

from app.events.publisher import publish_order_created


async def create_new_order(
    db: AsyncSession,
    order: OrderCreate,
):

    new_order = await create_order(
        db,
        order,
    )

    await publish_order_created(new_order)

    return new_order