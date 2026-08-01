from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    RABBITMQ_URL: str = "amqp://guest:guest@localhost/"


settings = Settings()