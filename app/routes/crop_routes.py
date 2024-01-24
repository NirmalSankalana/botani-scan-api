from fastapi import APIRouter, Depends, status, HTTPException, Response
from typing import List, Optional
from sqlalchemy.orm import Session

from ..schemas import crop_schema
from .. import models, oath2
from ..database import get_db

router = APIRouter(
    prefix="/crops",
    tags=['crops']
)


@router.get("/", response_model=List[crop_schema.Crop])
def get_crops(current_user: int = Depends(oath2.get_current_user), db: Session = Depends(get_db), limit: int = 40, skip: int = 0, search: Optional[str] = ""):
    crops = db.query(models.Crop).filter(
        models.Crop.title.contains(search)).limit(limit).offset(skip).all()
    return crops


@router.get("/{id}", response_model=crop_schema.Crop)
def get_crop(id: int, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):
    crop = db.query(models.Crop).filter(models.Crop.id == id).first()
    if crop == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"crop with {id} does not exists.")
    return crop


@router.post("/", response_model=crop_schema.Crop)
def create_crop(crop: crop_schema.CropCreate, db: Session = Depends(get_db), current_user_role: str = Depends(oath2.get_current_user_role)):
    oath2.has_required_role("admin", current_user_role)
    new_crop = models.Crop(**crop.dict())
    db.add(new_crop)
    db.commit()
    db.refresh(new_crop)
    return new_crop
