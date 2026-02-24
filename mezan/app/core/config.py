from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):

    #app
    app_name: str = "Mezan"
    app_version: str = "0.1.0"
    app_description: str = "Mezan API"
    app_host: str = "127.0.0.1"
    app_port: int = 8000

    #DB
    #postgres
    db_user: str = Field(default="postgres", env="POSTGRES_USER")
    db_password: str = Field(default="admin", env="POSTGRES_PASSWORD")
    db_name: str = Field(default="mezan_db", env="POSTGRES_DB")
    db_host: str = Field(default="postgres", env="POSTGRES_HOST")
    db_port: int = Field(default=5432, env="DB_PORT")

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
    

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()

