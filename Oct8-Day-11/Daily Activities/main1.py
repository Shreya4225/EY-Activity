from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    id: int
    name : str
    department : str
    salary : float

employees = [
    {"id": 1, "name": "Amit Sharma", "department": "HR", "salary": 50000},
    {"id": 2, "name": "Prajakta", "department": "ML", "salary": 60000},
]

@app.get("/employees")
def get_all():
    return employees

@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    for emp in employees:
        if emp["id"] == emp_id:
            return emp
    raise HTTPException(status_code=404, detail="employee not found")

@app.post("/employees", status_code=201)
def add_employee(employee: Employee):
    employees.append(employee.dict())
    return employee

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: Employee):
    for i,s in enumerate(employees):
        if s["id"] == employee_id:
            employees[i] = employee.dict()
            return employees[i]
    raise HTTPException(status_code=404, detail="employee not found")

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    for i,s in enumerate(employees):
        if s["id"] == employee_id:
            employees.pop(i)
            return{"message": "employee deleted successfully", "employee": s}
    raise HTTPException(status_code=404, detail="employee not found")






