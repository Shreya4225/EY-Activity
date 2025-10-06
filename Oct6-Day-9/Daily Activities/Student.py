from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    email: str
    is_active: bool= True

data = {"name": "Aisha", "age": 21, "email": "aish@example.com"}
student = Student(**data)

print(student)
print(student.name)
