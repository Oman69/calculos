from pydantic import BaseSettings


class Settings(BaseSettings):
    RABBITMQ_URL: str
    CELERY_RESULT_BACKEND: str

    class Config:
        env_file = ".env"


settings = Settings()