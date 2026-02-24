from fastapi import APIRouter, status
from app.schemas.health import Health


router = APIRouter()

@router.get("/", response_model = Health)
def health():
  massage = "OK"
  status_code = status.HTTP_200_OK
  return {"message": massage, "status_code": status_code}