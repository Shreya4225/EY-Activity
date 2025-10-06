class Student:
    def __init__(self, name, age, email):
        self.name=name
        self.age=age
        self.email=email

data= {"name": "Ali", "age": "twenty", "email": "abc@gmil"}
student = Student(**data)

print(student.age)