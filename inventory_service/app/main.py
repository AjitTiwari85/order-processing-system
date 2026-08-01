from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.session import engine
from app.models import Base

from app.events.consumer import start_consumer


@asynccontextmanager
async def lifespan(app: FastAPI):

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    connection = await start_consumer()

    yield

    await connection.close()


app = FastAPI(

    title="Inventory Service",

    lifespan=lifespan,
)


@app.get("/")
async def root():

    return {

        "service": "Inventory Service Running"

    }


@app.get("/health")
async def health():

    return {

        "status": "healthy"

    }