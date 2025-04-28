from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from argon2 import PasswordHasher
from app.core.security import create_access_token
from app.dependencies import SessionDep
from app.models.user import User, UserRegister
from app import crud
from app.config import settings
from app.models.token import Token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/create_user")
def create_user(session: SessionDep, form_data: Annotated[UserRegister, Depends()]):
    user = crud.get_user_by_email(session, form_data.email)
    if user:
        raise HTTPException(status_code=400, detail="User already exists")

    user = crud.create_user(session, form_data)
    return user


@router.post("/login")
def login(
    session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    user = crud.get_user_by_email(session, form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    user = crud.authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return Token(access_token=create_access_token(user.id, access_token_expires))
