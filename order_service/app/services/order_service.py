from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import OrderCreate
from app.repositories.order_repository import create_order


async def create_new_order(
    db: AsyncSession,
    order: OrderCreate,
):
    return await create_order(db, order)