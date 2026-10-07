from fastapi import FastAPI,status
from pydantic import BaseModel

app = FastAPI()

@app.post("/create-user",status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User Created"
    }
