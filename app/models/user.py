import uuid
from sqlmodel import Field, SQLModel
from pydantic import EmailStr


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, nullable=False)
    first_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    profile_picture_uri: str | None = Field(default=None)


class User(UserBase, table=True):
    id: uuid.UUID = Field(default=uuid.uuid4(), primary_key=True)
    hashed_password: str
    is_active: bool = Field(default=True)


class UserRegister(SQLModel):
    email: EmailStr = Field(unique=True, nullable=False)
    password: str = Field(min_length=8, max_length=40)
    first_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)


class UserPublic(UserBase):
    id: uuid.UUID
