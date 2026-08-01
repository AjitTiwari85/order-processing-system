from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DATABASE_URL: str = (
        "postgresql+asyncpg://postgres:postgres@localhost:5434/inventorydb"
    )

    RABBITMQ_URL: str = (
        "amqp://guest:guest@localhost/"
    )


settings = Settings()