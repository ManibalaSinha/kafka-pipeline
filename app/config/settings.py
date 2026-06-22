from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # adjust if needed

class Settings(BaseSettings):

    APP_NAME: str
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    KAFKA_BOOTSTRAP_SERVER: str

    REDIS_HOST: str
    REDIS_PORT: int
   
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
settings = Settings()
