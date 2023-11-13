# botani-scan-api

## How to set up the project.

1. Install python 3.8 or above if not available
2. Create virtual environment name env in the project folder : `python -m venv .venv`
3. Move to the project folder and activate virtual environment :
   - in Mac and Linux :source .venv/bin/activate
   - in Windows : run activate.bat file which is inside \env\Scripts folder by running `.venv\Scripts\activate`
4. Install required libraries : `pip3 install -r requirements.txt`
5. After stop the project, deactivate virtual environment : deactivate

## Run project
1. uvicorn `uvicorn app.main:app --reload`
2. Swagger documentation is available at : `http://{host}:{port}/docs#` 

## Save Dependancies
1. Run `pip3 freeze > requirements.txt` after installing any pip package