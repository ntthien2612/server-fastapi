from fastapi import Depends, HTTPException, status
import jwt
from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas import user_schema
from .. import models
from ..core import security
from ..core.security import hash_password
from fastapi.security import OAuth2PasswordBearer
from ..core import database
from jwt import PyJWTError as JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: user_schema.UserCreate):
    hashed_password = security.hash_password(user.password)
    new_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
        
def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not security.verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(email: str):
    return security.create_access_token({"sub": email})


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, security.SECRET_KEY, algorithms=[security.ALGORITHM])
        email : str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user_by_email(db, email)
    if user is None:
        raise credentials_exception
    return user