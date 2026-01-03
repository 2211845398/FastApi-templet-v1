from services.auth_service import AuthService
from fastapi import APIRouter, Depends
from schemas.users import UserCreate, UserLogin
from sqlalchemy.orm import Session
from db.database import get_db


router = APIRouter()

@router.post("/register")
def register(user:UserCreate, db: Session = Depends(get_db)):
    return AuthService.create_user(db,user)

@router.post("/login")
def login(credentials:UserLogin, db: Session = Depends(get_db)):
    return AuthService.authenticate_user(db,credentials)

@router.get("/me")
def get_current_user(token: str, db: Session = Depends(get_db)):
    return AuthService.get_current_user(db,token)

@router.get("/user/{email}")
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    return AuthService.get_user_by_email(db,email)
    