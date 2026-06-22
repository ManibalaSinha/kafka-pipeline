from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "KafkaPipeline"

    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    kafka_bootstrap_server: str
    redis_host: str = "localhost"
    redis_port: int = 6379

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache()
def get_settings():
    return Settings()

""" from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "KafkaPipeline"
    DATABASE_URL: str
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    REDIS_URL: str = "redis://localhost:6379"

    class Config:
        env_file = ".env"

settings = Settings() """