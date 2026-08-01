from fastapi import FastAPI

from .database import engine
from .models import Base

from .api.orders import router as order_router

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


# Register Orders Router
app.include_router(order_router)