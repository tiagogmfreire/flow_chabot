from fastapi import FastAPI, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from controllers.APIController import APIController
from services.rag_service import RagService
from services.flow_service import FlowService
from models.vector_model import VectorModel
from services.chat_service import ChatService
import shutil
import json

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4321",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        file_location = f"uploaded_files/rag.pdf"
        
        # Create the directory if it doesn't exist (optional, but good practice)
        import os
        os.makedirs("uploaded_files", exist_ok=True)

        # Save the uploaded file in chunks to handle large files efficiently
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        vector = VectorModel()
        rag = RagService(vector)
        rag.parse_doc(file_path=file_location)
        
        return {"message": f"Successfully uploaded {file.filename}", "location": file_location}
    except Exception as e:
        return {"message": f"There was an error uploading the file: {e}"}
    finally:
        # Ensure the file handle is closed
        file.file.close()

@app.post("/chat")
async def chat(request: Request):

    body = await request.body()

    string = json.loads(body)

    prompt = string['chat']

    vector = VectorModel()
    rag = RagService(vector)
    flow = FlowService()

    chat = ChatService(rag, flow)

    response = chat.chat(prompt)
    
    return {"message": response}