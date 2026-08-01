from fastapi import FastAPI

from app.db.session import engine

from app.models import Base

app = FastAPI(
    title="Inventory Service"
)


@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:

        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():

    return {
        "service": "Inventory Service"
    }