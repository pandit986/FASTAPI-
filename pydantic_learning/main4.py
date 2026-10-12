
# Exception Handling in FastAPI

# Import FastAPI to create the application
# HTTPException to raise built-in HTTP errors
# Request to access details of the incoming request
from fastapi import FastAPI, HTTPException, Request

# JSONResponse is used to return a custom JSON error response
from fastapi.responses import JSONResponse

# Create the FastAPI application
app = FastAPI()


# 1. Create a custom exception class
# We use this when a user is not found in our application
class UserNotFoundException(Exception):

    # Constructor accepts the user's name
    def __init__(self, name: str):
        # Store the name so we can use it in the error message
        self.name = name


# 2. Global Exception Handler
# This handler catches UserNotFoundException
# raised anywhere in the application
@app.exception_handler(UserNotFoundException)
def user_not_found_handle(
    request: Request,
    exc: UserNotFoundException
):
    # request contains details of the incoming HTTP request
    # exc contains details of the exception that was raised
    print(request)

    # Return a custom JSON error response to the client
    return JSONResponse(
        status_code=404,  # HTTP 404 means Resource Not Found
        content={
            # Display the name received in the exception
            "message": f"User with name {exc.name} not found"
        }
    )


# 3. GET endpoint to find a user by name
# Example URL: /user/Abhishek
@app.get("/user/{name}")
def get_details(name: str):

    # Check whether the requested name matches our user
    if name != "Abhishek":

        # Raise our custom exception if the user is not found
        # FastAPI will call the registered exception handler
        raise UserNotFoundException(name)

    # If the name matches, return the user's details
    return {
        "name": name
    }


# 4. GET endpoint to find a user by ID
# Example URL: /users/1
@app.get("/users/{user_id}")
def get_user(user_id: int):

    # Check whether the requested user ID is valid
    if user_id != 1:

        # Raise FastAPI's built-in HTTPException
        # No custom handler is needed for this example
        raise HTTPException(
            status_code=404,  # HTTP 404 means Resource Not Found
            detail="user Not Found"
        )

    # If the ID matches, return the user's details
    return {
        "Message": "user Found",
        "data": {
            "name": "Abhishek"
        }
    }
