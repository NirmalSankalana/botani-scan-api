from fastapi import APIRouter, Depends, status, HTTPException, Response
from typing import List, Optional
from sqlalchemy.orm import Session

from ..schemas import user_schema
from .. import models
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['users']
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
