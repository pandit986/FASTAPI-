
from pydantic import BaseModel, ConfigDict, EmailStr, Field


# Schema for creating a user
class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    age: int = Field(ge=1, le=120)


# Schema for updating a user
class UserUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    age: int = Field(ge=1, le=120)


# Schema for returning a user
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int

    model_config = ConfigDict(from_attributes=True)
