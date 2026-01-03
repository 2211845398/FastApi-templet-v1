from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    #app
    app_name: str = "Big FastAPI"
    app_version: str = "0.1.0"
    app_description: str = "Big FastAPI to learn more about FastAPI"
    app_port: int = 5555
    app_host: str = "0.0.0.0"

    #database
    db_user: str = Field(default="postgres", env="POSTGRES_USER")
    db_password: str = Field(default="postgres", env="POSTGRES_PASSWORD")
    db_host: str = Field(default="localhost", env="DB_HOST")
    db_port: int = Field(default=5432, env="DB_PORT")
    db_name: str = Field(default="fastapi_auth", env="POSTGRES_DB")
    
    @property
    def database_url(self):
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
    
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    redis_url: str = Field(..., env="REDIS_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()