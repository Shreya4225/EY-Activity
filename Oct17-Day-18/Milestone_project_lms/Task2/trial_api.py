from fastapi import FastAPI, HTTPException
import pandas as pd
from pydantic import BaseModel

# Pydantic models
class Student(BaseModel):
    StudentID: str
    Name: str
    Email: str
    Country: str

class Course(BaseModel):
    CourseID: str
    Title: str
    Category: str
    Duration: int

# Create FastAPI instance
app = FastAPI()

# Load CSV data
students = pd.read_csv("../students.csv").to_dict(orient="records")
courses = pd.read_csv("../courses.csv").to_dict(orient="records")

# STUDENT ENDPOINTS
@app.get("/students")
def get_all_students():
    return {"students": students}

@app.post("/students", status_code=201)
def add_student(student: Student):
    if any(s["StudentID"] == student.StudentID for s in students):
        raise HTTPException(status_code=400, detail="Student already exists")
    students.append(student.dict())
    pd.DataFrame(students).to_csv("../students.csv", index=False)
    return {"message": "Student added successfully", "student": student}

@app.put("/students/{student_id}")
def update_student(student_id: str, updated_student: Student):
    for i, s in enumerate(students):
        if s["StudentID"] == student_id:
            students[i] = updated_student.dict()
            pd.DataFrame(students).to_csv("../students.csv", index=False)
            return {"message": "Student updated successfully", "student": updated_student}
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
def delete_student(student_id: str):
    for i, s in enumerate(students):
        if s["StudentID"] == student_id:
            students.pop(i)
            pd.DataFrame(students).to_csv("../students.csv", index=False)
            return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")

# COURSE ENDPOINTS
@app.get("/courses")
def get_all_courses():
    return {"courses": courses}

@app.post("/courses", status_code=201)
def add_course(course: Course):
    if any(c["CourseID"] == course.CourseID for c in courses):
        raise HTTPException(status_code=400, detail="Course already exists")
    courses.append(course.dict())
    pd.DataFrame(courses).to_csv("../courses.csv", index=False)
    return {"message": "Course added successfully", "course": course}

@app.put("/courses/{course_id}")
def update_course(course_id: str, updated_course: Course):
    for i, c in enumerate(courses):
        if c["CourseID"] == course_id:
            courses[i] = updated_course.dict()
            pd.DataFrame(courses).to_csv("../courses.csv", index=False)
            return {"message": "Course updated successfully", "course": updated_course}
    raise HTTPException(status_code=404, detail="Course not found")

@app.delete("/courses/{course_id}")
def delete_course(course_id: str):
    for i, c in enumerate(courses):
        if c["CourseID"] == course_id:
            courses.pop(i)
            pd.DataFrame(courses).to_csv("../courses.csv", index=False)
            return {"message": "Course deleted successfully"}
    raise HTTPException(status_code=404, detail="Course not found")
