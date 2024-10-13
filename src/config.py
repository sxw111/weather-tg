from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    TG_API_TOKEN: str
    WEATHER_API_TOKEN: str


settings = Settings()
