from fastapi import APIRouter, Depends, status, HTTPException, responses
from sqlalchemy.orm import session

from .. import database, models, utils

from ..schemas import user_login

router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(user_credentials: user_login.UserLogin, db: session = Depends(database.get_db)):
    user = db.query(models.User).filter(
        models.User.email == user_credentials.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")

    return {"token": "adsada"}
