from fastapi import APIRouter, Depends

from app.db.database import get_db
from app.schemas.user import UserCreate, UserLogin
from sqlalchemy.orm import Session

from app.services.auth_service import Authservice


router = APIRouter()

@router.post("/register")
def register(user:UserCreate, db: Session = Depends(get_db)):
    return Authservice.create_user(db, user)

@router.post("/login")
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    return Authservice.authenticate_user(db, credentials)

@router.get("/me")
def get_current_user(token: str , db: Session = Depends(get_db)):
    return Authservice.get_current_user(db, token)

@router.get("/user/{email}")
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    return Authservice.get_user_by_email(db, email)



