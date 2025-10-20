from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Course(BaseModel):
    CourseID: str
    Title: str
    Category: str
    Duration: int


class Student(BaseModel):
    StudentID: str
    Name: str
    Email: str
    Country: str


courses = [
    Course(CourseID="C101", Title="Python for Beginners", Category="Programming", Duration=40),
    Course(CourseID="C102", Title="Machine Learning Basics", Category="AI", Duration=60),
    Course(CourseID="C103", Title="Data Visualization with Power BI", Category="Analytics", Duration=30),
    Course(CourseID="C104", Title="Cloud Fundamentals", Category="Cloud", Duration=50),
]

students = [
    Student(StudentID="S001", Name="Neha", Email="neha@example.com", Country="India"),
    Student(StudentID="S002", Name="Arjun", Email="arjun@example.com", Country="UAE"),
    Student(StudentID="S003", Name="Sophia", Email="sophia@example.com", Country="UK"),
    Student(StudentID="S004", Name="Ravi", Email="ravi@example.com", Country="India"),
    Student(StudentID="S005", Name="Meena", Email="meena@example.com", Country="USA"),
]


@app.get("/courses")
def get_all_courses():
    return courses


@app.post("/courses")
def add_course(course: Course):
    courses.append(course)
    return {"message": "Course added successfully", "course": course}


@app.put("/courses/{id}")
def update_course(id: str, updated_course: Course):
    for i in range(len(courses)):
        if courses[i].CourseID == id:
            courses[i] = updated_course
            return {"message": "Course updated successfully", "course": updated_course}
    raise HTTPException(status_code=404, detail="course not found")


@app.delete("/courses/{id}")
def delete_course(id: str):
    for i in range(len(courses)):
        if courses[i].CourseID == id:
            del courses[i]
            return {"message": "Course deleted successfully"}
    raise HTTPException(status_code=404, detail="course not found")


@app.get("/students")
def get_all_students():
    return students


@app.post("/students")
def add_student(student: Student):
    students.append(student)
    return {"message": "Student added successfully", "student": student}


@app.put("/students/{id}")
def update_student(id: str, updated_student: Student):
    for i in range(len(students)):
        if students[i].StudentID == id:
            students[i] = updated_student
            return {"message": "Student updated successfully", "student": updated_student}
    raise HTTPException(status_code=404, detail="student not found")


@app.delete("/students/{id}")
def delete_student(id: str):
    for i in range(len(students)):
        if students[i].StudentID == id:
            del students[i]
            return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="student not found")
