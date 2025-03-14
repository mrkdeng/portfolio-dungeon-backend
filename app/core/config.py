from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    server_ip: str = "0.0.0.0"
    port: int = 8000
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()