
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DJANGO_SECRET_KEY: str = 'drink_recommend'
    DEBUG: bool = True
    ALLOWED_HOSTS: list[str] = []

    POSTGRES_DB: str = 'drink_recommend'
    POSTGRES_USER: str = 'drink_recommend'
    POSTGRES_PASSWORD: str = 'drink_recommend'
    POSTGRES_HOST: str = 'db'
    POSTGRES_PORT: int = 5432

    REDIS_PASSWORD: str = 'drink_recommend'

    FLOWER_USER: str = 'drink_recommend'
    FLOWER_PASSWORD: str = 'drink_recommend'

    SMTP_GMAIL_USER: str = ''
    SMTP_GMAIL_PASSWORD: str = ''
    
    LLM_API_KEY: str = ''

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
