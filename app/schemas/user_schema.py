from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    user_type: str


class UserCreate(UserBase):
    password: str
    user_type: str


class UserOut(UserBase):
    id: int
