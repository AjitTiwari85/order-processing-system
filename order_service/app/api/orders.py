from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas import OrderCreate, OrderResponse
from app.services.order_service import create_new_order

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post(
    "",
    response_model=OrderResponse,
    status_code=201
)
async def create_order(
    order: OrderCreate,
    db: AsyncSession = Depends(get_db),
):
    return await create_new_order(db, order)