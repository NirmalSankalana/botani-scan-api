import os
from fastapi import APIRouter, Depends, HTTPException
import pandas as pd
from sqlalchemy.orm import Session

from ..schemas import crop_schema
from .. import models
from ..database import get_db

router = APIRouter(
    prefix="/seed",
    tags=['seed']
)


@router.post("/", response_model=crop_schema.Crop)
def seed_data(db: Session = Depends(get_db)):
    try:
        # Get the directory containing the current script
        script_directory = os.path.dirname(os.path.abspath(__file__))

        # Construct the absolute path to the CSV file
        file_path = os.path.join(script_directory.strip(
            '\\routes'), 'data', 'crops_dataset.csv')

        # Print the paths for debugging
        print("Script directory:", script_directory)
        print("File path:", file_path)

        # Check if the file exists
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="CSV file not found")

        # Read the CSV file
        crops = pd.read_csv(file_path)

        for index, row in crops.iterrows():
            new_crop = models.Crop(**row.to_dict())
            db.add(new_crop)

        db.commit()
        db.refresh(new_crop)
        return "data added successfully"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
