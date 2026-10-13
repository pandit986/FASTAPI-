
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Employee(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    emp_code: int
    address: str
    age: int


# Schema for partial updates
class EmployeeUpdate(BaseModel):
    name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    address: str | None = None
    age: int | None = None


employees = [
    {
        "name": "Abhishek",
        "last_name": "Pandit",
        "email": "abhishek@example.com",
        "emp_code": 101,
        "address": "Navi Mumbai, Maharashtra",
        "age": 25
    },
    {
        "name": "Rahul",
        "last_name": "Sharma",
        "email": "rahul@example.com",
        "emp_code": 102,
        "address": "Pune, Maharashtra",
        "age": 28
    },
    {
        "name": "Amit",
        "last_name": "Patil",
        "email": "amit@example.com",
        "emp_code": 103,
        "address": "Mumbai, Maharashtra",
        "age": 30
    },
    {
        "name": "Priya",
        "last_name": "Shah",
        "email": "priya@example.com",
        "emp_code": 104,
        "address": "Thane, Maharashtra",
        "age": 26
    },
    {
        "name": "Sneha",
        "last_name": "Joshi",
        "email": "sneha@example.com",
        "emp_code": 105,
        "address": "Nashik, Maharashtra",
        "age": 27
    }
]


@app.post("/create-employee", status_code=201)
def create_employee(employee: Employee):
    for emp in employees:
        if employee.emp_code == emp["emp_code"]:
            raise HTTPException(
                status_code=400,
                detail="Employee with this emp_code already exists"
            )

    new_employee = employee.model_dump()
    employees.append(new_employee)

    return {
        "message": "Employee created successfully",
        "data": new_employee
    }


@app.get("/get-employee-id/{emp_code}")
def get_employee(emp_code: int):
    for emp in employees:
        if emp["emp_code"] == emp_code:
            return {
                "message": "Employee retrieved successfully",
                "data": emp
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


@app.get("/get-all-employee")
def get_all_employee():
    return {
        "message": "Employees retrieved successfully",
        "data": employees
    }


@app.patch("/update-employee/{emp_code}")
def update_employee(emp_code: int, employee: EmployeeUpdate):
    for index, emp in enumerate(employees):
        if emp["emp_code"] == emp_code:
            update_data = employee.model_dump(exclude_unset=True)

            employees[index].update(update_data)

            return {
                "message": "Employee updated successfully",
                "data": employees[index]
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

app.delete("/delete-employee/{emp_code}")
def delete_employee(emp_code: int):
    for index, emp in enumerate(employees):
        if emp["emp_code"] == emp_code:
            deleted_employee = employees.pop(index)
            return {
                "message": "Employee deleted successfully",
                "data": deleted_employee
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )



@app.get("/")
def home():
    return {"message": "Hello, World!"}