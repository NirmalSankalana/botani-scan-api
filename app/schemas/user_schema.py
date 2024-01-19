from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr

class UserLogin(UserBase):
    password: str


class UserCreate(UserBase):
    password: str
    user_type: str


class UserOut(UserBase):
    id: int
