from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.events.consumer import start_consumer


@asynccontextmanager
async def lifespan(app: FastAPI):

    connection = await start_consumer()

    yield

    await connection.close()


app = FastAPI(
    title="Notification Service",
    lifespan=lifespan,
)


@app.get("/")
async def root():

    return {
        "message": "Notification Service Running"
    }