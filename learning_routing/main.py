from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home_route():
    return {"message":" "}

@app.get('/user/{user_id}')
def get_user_detail(user_id:int):
    if user_id == 10:
        return {
            "name":"Abhishek"
        }
    else:
        return{"user_id":user_id}


@app.get("/employes")
def get_emplpoye_details(name:str = None):
    print(name)
    return {
        "name":name
    }


