from fastapi import APIRouter, Depends, status, HTTPException, Response
from typing import List, Optional
from sqlalchemy.orm import Session

from ..schemas import crop_schema
from .. import models
from ..database import get_db

router = APIRouter(
    prefix="/crops",
    tags=['crops']
)


@router.get("/", response_model=List[crop_schema.Crop])
def get_posts(db: Session = Depends(get_db), limit: int = 40, skip: int = 0, search: Optional[str] = ""):
    crops = db.query(models.Crop).filter(
        models.Crop.title.contains(search)).limit(limit).offset(skip).all()
    return crops


@router.get("/{id}", response_model=crop_schema.Crop)
def get_post(id: int, db: Session = Depends(get_db)):
    crop = db.query(models.Crop).filter(models.Crop.id == id).first()
    if crop == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"crop with {id} does not exists.")
    return crop
