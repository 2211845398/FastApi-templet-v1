from fastapi import APIRouter, status
from schemas.health import Health
router = APIRouter()

@router.get("/", response_model=Health)
def health():
    message = "OK"
    status_code = status.HTTP_200_OK
    return {"message": message, "status_code": status_code}