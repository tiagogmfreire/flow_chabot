from fastapi import FastAPI
from flow import generate_token

app = FastAPI()

@app.get("/")
async def root():

    token = generate_token()

    return {"message": token}
