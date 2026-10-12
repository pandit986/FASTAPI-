from fastapi import FastAPI, Depends, Header, HTTPException,Request
import time

app = FastAPI()


@app.middleware("http")
async def logging_middleware(request:Request,call_next):
    start_time = time.time()

    response = await call_next(request) 

    process_time = time.time() - start_time

    print(f"Request: {request.method} {request.url} completed in {process_time:.4f} seconds")
    return response


# @app.middleware("http")
# async def my_middleware(request:Request, call_next):
#     print("Middleware executed before request processing")
#     response = await call_next(request)
#     print("Middleware executed after request processing")
#     return response