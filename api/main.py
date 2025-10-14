from fastapi import FastAPI, File, UploadFile
from typing import Annotated
from controllers.APIController import APIController
import shutil

app = FastAPI()

@app.get("/")
async def root():

    return APIController.index()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    """
    Uploads a single file and saves it to the server.
    """
    try:
        # Define the path where the file will be saved
        file_location = f"uploaded_files/{file.filename}"
        
        # Create the directory if it doesn't exist (optional, but good practice)
        import os
        os.makedirs("uploaded_files", exist_ok=True)

        # Save the uploaded file in chunks to handle large files efficiently
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return {"message": f"Successfully uploaded {file.filename}", "location": file_location}
    except Exception as e:
        return {"message": f"There was an error uploading the file: {e}"}
    finally:
        # Ensure the file handle is closed
        file.file.close()