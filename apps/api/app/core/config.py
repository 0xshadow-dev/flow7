from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    #Database
    database_url: str = "postgresql://flow7_user:flow7_password@localhost:5432/flow7"

    #API
    api_v1_str: str = "/api/v1"
    project_name: str = "FLow7 API"

    #Environment
    environment: str = "development"
    debug: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = True

# Global settings instance
settings = Settings()
