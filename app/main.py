from fastapi import FastAPI

from . import models
from .database import engine, get_db
from .config import settings

from .routes import crop_routes, user_routes, seed_routes, prediction_routes, auth


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def test():
    return {"message": "This is a test end point"}

app.include_router(crop_routes.router)
app.include_router(user_routes.router)
app.include_router(seed_routes.router)
app.include_router(prediction_routes.router)
app.include_router(auth.router)
