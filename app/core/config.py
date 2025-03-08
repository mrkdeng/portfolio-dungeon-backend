from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    server_ip: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"  # Use .env file for loading environment variables

settings = Settings()
