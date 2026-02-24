from fastapi import HTTPException
from app.models.user import User
from app.schemas.user import UserLogin, UserResponse, UserCreate
from sqlalchemy.orm import Session
from uuid import UUID
from app.utils.security import hash_password, verify_password, create_access_token, decode_access_token


class Authservice:
    
    @staticmethod
    def create_user(db: Session, user: UserCreate) -> UserResponse:
      existing_user = db.query(User).filter(
         ((User.email == user.email) | (User.username == user.username)).first()
      )

      if existing_user:
         raise HTTPException(status_code=400, detail="user already exists")
      
      hashed_password = hash_password(user.password)
      new_user = User(
         email=user.email,
         username=user.username,
         hashed_password=hashed_password
      )

      db.add(new_user)
      db.commit()
      db.refresh(new_user)

      return UserResponse(
          id = new_user.id,
          email = new_user.email,
          username = new_user.username,
          is_active = new_user.is_active,
          created_at = new_user.created_at,
          updated_at = new_user.updated_at
      )
    

    @staticmethod
    def authenticate_user(db: Session, credentials: UserLogin) -> dict:
       user = db.query(User).filter(
          (User.email == credentials.email).first() 
       )

       if not user:
          raise HTTPException(status_code=401, detail="Invalid email or password")
       
       if not verify_password(credentials.password, user.hashed_password):
          raise HTTPException(status_code=401, detail="Invalid email or password")
       
       if not user.is_active:
          raise HTTPException(status_code=401, detail="User account is inactive")
       
       accsess_token = create_access_token(data={"sub": str(user.id)})
       
       return {
          "access_token": accsess_token,
          "token_type": "bearer",
          "user": UserResponse(
             id = user.id,
             email = user.email,
             username = user.username,
             is_active = user.is_active,
             created_at = user.created_at,
             updated_at = user.updated_at
          )
       }
    
    @staticmethod
    def get_current_user(db: Session, token: str) -> UserResponse:
       payload = decode_access_token(token)

       if not payload:
          raise HTTPException(status_code=401, detail="Invalid token")
       
       user_id_str = payload.get("sub")
       if not user_id_str:
          raise HTTPException(status_code=401, detail="Invalid token")
       
       # Convert user_id to UUID
       try: 
          user_id = UUID(user_id_str)
       except (ValueError, TypeError):
          raise HTTPException(status_code=401, detail="Invalid token format")
       

       user = db.query(User).filter(User.id == user_id).first()

       if not user:
          raise HTTPException(status_code=401, detail="User not found")
       if not user.is_active:
          raise HTTPException(status_code=401, detail="User account is inactive")
       
       return UserResponse(
          id = user.id,
          email = user.email,
          username = user.username,
          is_active = user.is_active,
          created_at = user.created_at,
          updated_at = user.updated_at
       )
    

    @staticmethod
    def get_user_by_email(db: Session, email: str):
       return db.query(User).filter(User.email == email).first()
      

      
    

          
        

