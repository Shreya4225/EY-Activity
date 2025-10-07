from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
class Employee(BaseModel):
    id: int
    name : str
    department : str
    salary : float

employees = [
    {"id": 1, "name": "Atharva", "department": "AI", "salary": "AI"},
    {"id": 2, "name": "Prajakta", "department": "ML", "salary": "ML"},
]

@app.get("/employees")
def get_employees():
    return {"employees" : employees}

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="student not found")

@app.post(path= "/employees", status_code=201)
def add_employee(employee: Employee):
    employees.append(employee.dict())
    return{"message": "employee added successfully", "employee": employee}

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: Employee):
    for i, s in enumerate(employees):
        if s["id"] == employee_id:
            employees[i] = updated_employee.dict()
            return{"message": "employee updated successfully", "employee": employees[i]}
    raise HTTPException(status_code=404, detail="employee not found")

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    for i, s in enumerate(employees):
        if s["id"] == employee_id:
            employees.pop(i)
            return{"message": "employee deleted successfully", "employee": s}
    raise HTTPException(status_code=404, detail="employee not found")




