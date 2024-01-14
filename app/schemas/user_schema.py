from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    password: str


class UserCreate(UserBase):
    user_type: str
