from fastapi import FastAPI
import sqlite3
import pandas as pd

app = FastAPI(title="LMS API (SQL Version)")
DB = "lms.db"

def query(sql, params=(), fetch=False):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(sql, params)
    if fetch:
        data = cur.fetchall()
        conn.close()
        return data
    conn.commit()
    conn.close()
    return {"status": "ok"}

@app.get("/courses")
def get_courses():
    df = pd.read_sql("SELECT * FROM courses", sqlite3.connect(DB))
    return df.to_dict(orient="records")

@app.post("/courses")
def add_course(course: dict):
    return query("INSERT OR REPLACE INTO courses VALUES (?,?,?,?)",
                 (course['CourseID'], course['Title'], course['Category'], course['Duration']))

@app.put("/courses/{course_id}")
def update_course(course_id: str, course: dict):
    return query("UPDATE courses SET Title=?, Category=?, Duration=? WHERE CourseID=?",
                 (course['Title'], course['Category'], course['Duration'], course_id))

@app.delete("/courses/{course_id}")
def delete_course(course_id: str):
    return query("DELETE FROM courses WHERE CourseID=?", (course_id,))

@app.get("/students")
def get_students():
    df = pd.read_sql("SELECT * FROM students", sqlite3.connect(DB))
    return df.to_dict(orient="records")

@app.post("/students")
def add_student(student: dict):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO students VALUES (?,?,?,?)",
                (student['StudentID'], student['Name'], student['Email'], student['Country']))
    conn.commit()
    conn.close()
    return {"status": "Student added successfully"}

@app.put("/students/{student_id}")
def update_student(student_id: str, student: dict):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("UPDATE students SET Name=?, Email=?, Country=? WHERE StudentID=?",
                (student['Name'], student['Email'], student['Country'], student_id))
    conn.commit()
    conn.close()
    return {"status": "Student updated successfully"}

@app.delete("/students/{student_id}")
def delete_student(student_id: str):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE StudentID=?", (student_id,))
    conn.commit()
    conn.close()
    return {"status": "Student deleted successfully"}

