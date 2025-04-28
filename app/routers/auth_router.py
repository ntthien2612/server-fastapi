from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..core import database
from ..schemas import user_schema as schemas
from ..services import auth_service as services

router = APIRouter()

@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    existing_user = services.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = services.create_user(db, user)
    return new_user

@router.post("/login", response_model=schemas.TokenResponse)
def login(user_data : schemas.UserLogin, db: Session = Depends(database.get_db)):
    user = services.authenticate_user(db, user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    user = schemas.UserResponse(id=user.id, username=user.username, email=user.email)

    token = services.create_access_token(user.email)
    return {"access_token": token, "token_type": "bearer"}