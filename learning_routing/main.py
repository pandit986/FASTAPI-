from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home_route():
    return {"message":"how are you bro"}

@app.get('/user/{user_id}')
def get_user_detail(user_id):
    if user_id == 10:
        return {
            "name":"Abhishek"
        }
    else:
        return{"user_id":user_id}