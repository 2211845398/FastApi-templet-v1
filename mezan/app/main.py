from fastapi import FastAPI
from app.Api.endPoints import main_router
from app.core.config import settings


app = FastAPI(
  title = settings.app_name,
  version = settings.app_version,
  description = settings.app_description
)

app.include_router(main_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = settings.app_host, port = settings.app_port)

