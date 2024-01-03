from fastapi import FastAPI

from . import models
from .database import engine, get_db
from .config import settings

from .routes import crop_routes
from .routes import seed_routes
from .routes import prediction_routes

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def test():
    return {"message": "This is a test end point"}

app.include_router(crop_routes.router)
app.include_router(seed_routes.router)
app.include_router(prediction_routes.router)
