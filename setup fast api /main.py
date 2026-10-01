from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Message":"hello ji kaise ho app log "}