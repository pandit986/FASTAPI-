from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    user_name:str
    phone_number:int

class ResponseSchema(BaseModel):
    message:str
    data:User

@app.post("/create-user",status_code=status.HTTP_201_CREATED,response_model=ResponseSchema)
def create_user(user:User):
    print(user)
    return {
        "message": "User Created",
        "data" : user
    }

@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(status_code=404,detail="User Not Found")
    return{
        "id":1,
        "name":"SuperAdmin"
    }