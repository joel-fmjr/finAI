from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Base settings
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    DEBUG: bool = True
    SECRET_KEY: str
    ALLOWED_HOSTS: list[str] = ['*']

    # Database settings
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

    # Redis settings
    REDIS_HOST: str = 'localhost'
    REDIS_PORT: int = 6379

    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', case_sensitive=True
    )

    @property
    def DATABASES(self) -> dict:
        return {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': self.DB_NAME,
                'USER': self.DB_USER,
                'PASSWORD': self.DB_PASSWORD,
                'HOST': self.DB_HOST,
                'PORT': self.DB_PORT,
            }
        }


settings = Settings()
