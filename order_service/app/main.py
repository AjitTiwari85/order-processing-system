from fastapi import FastAPI, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from .database import engine, get_db
from .models import Base, Order
from .schemas import OrderCreate, OrderResponse

app = FastAPI(
    title="Order Service",
    version="1.0.0"
)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    return {
        "message": "Order Service Running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }


@app.post(
    "/orders",
    response_model=OrderResponse,
    status_code=201
)
async def create_order(
    order: OrderCreate,
    db: AsyncSession = Depends(get_db)
):
    new_order = Order(
        customer_name=order.customer_name,
        product_name=order.product_name,
        quantity=order.quantity
    )

    db.add(new_order)

    await db.commit()

    await db.refresh(new_order)

    return new_order