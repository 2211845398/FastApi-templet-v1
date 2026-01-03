from api.v1 import health, auth
from fastapi import APIRouter

main_router = APIRouter()

main_router.include_router(health.router, prefix="/check", tags=["Health"])
main_router.include_router(auth.router, prefix="/auth", tags=["Auth"])