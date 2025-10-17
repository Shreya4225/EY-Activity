import sqlite3
import pandas as pd

DB = "lms.db"


def create_tables():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    # Courses table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        CourseID TEXT PRIMARY KEY,
        Title TEXT,
        Category TEXT,
        Duration INTEGER
    )''')

    # Students table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS students (
        StudentID TEXT PRIMARY KEY,
        Name TEXT,
        Email TEXT,
        Country TEXT
    )''')

    # Enrollments table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS enrollments (
        EnrollmentID TEXT PRIMARY KEY,
        StudentID TEXT,
        CourseID TEXT,
        EnrollDate TEXT,
        Progress INTEGER,
        FOREIGN KEY(StudentID) REFERENCES students(StudentID),
        FOREIGN KEY(CourseID) REFERENCES courses(CourseID)
    )''')

    conn.commit()
    conn.close()
    print("Tables created successfully!")


def load_csv_to_db():
    conn = sqlite3.connect(DB)

    # Load courses
    courses = pd.read_csv("data/courses.csv")
    courses.to_sql("courses", conn, if_exists="replace", index=False)

    # Load students
    students = pd.read_csv("data/students.csv")
    students.to_sql("students", conn, if_exists="replace", index=False)

    # Load enrollments
    enrollments = pd.read_csv("data/enrollments.csv")
    enrollments.to_sql("enrollments", conn, if_exists="replace", index=False)

    conn.close()
    print("CSV data loaded into database!")


if __name__ == "__main__":
    create_tables()
    load_csv_to_db()
