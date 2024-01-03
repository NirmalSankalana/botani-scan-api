import os
from fastapi import FastAPI, File, UploadFile, APIRouter
from fastapi.responses import JSONResponse
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

from sqlalchemy.orm import Session
import io  # Import io module

router = APIRouter(
    prefix="/predictions",
    tags=['predictions']
)

# Load the saved model


def load_efficientnet():
    try:
        script_directory = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(script_directory.strip(
            '\\routes'), 'model', 'efficientnetv2s_fine_tuned.h5')
        model = load_model(model_path)
        print("Model loaded successfully")
        return model
    except:
        print("Could not load model")


def preprocess_image(file_content):  # Modify the function to accept file content
    img = image.load_img(io.BytesIO(file_content), target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array


@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        img_array = preprocess_image(await file.read())  # Read file content
        # Make predictions
        model = load_efficientnet()
        predictions = model.predict(img_array)
        # Convert to standard Python int
        predicted_class = int(np.argmax(predictions[0]))

        return JSONResponse(content={"class_id": predicted_class, "class_name": str(predicted_class)}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
