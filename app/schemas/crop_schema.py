from pydantic import BaseModel
from datetime import datetime


class CropBase(BaseModel):
    title: str
    description: str
    image_id: str


class CropCreate(CropBase):
    pass


class Crop(CropBase):
    id: int
    created_at: datetime
    # Ensure creating ORM friendly schema

    class Config:
        orm_mode = True
