from fastapi import FastAPI
from controllers.APIController import APIController
app = FastAPI()

@app.get("/")
async def root():

    return APIController.index()
