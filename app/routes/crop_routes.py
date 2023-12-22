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
    print("crop routes called")
    crops = db.query(models.Crop).filter(
        models.Crop.title.contains(search)).limit(limit).offset(skip).all()
    return crops
