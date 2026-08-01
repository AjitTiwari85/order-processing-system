from fastapi import FastAPI

from .database import engine
from .models import Base

app = FastAPI()


@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    return {"message": "Order Service Running"}


@app.get("/health")
async def health():
    return {"status": "healthy"}