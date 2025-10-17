import sqlite3
import pandas as pd

DB = "lms.db"


def process_enrollments():
    conn = sqlite3.connect(DB)

    # Load tables
    students = pd.read_sql("SELECT * FROM students", conn)
    courses = pd.read_sql("SELECT * FROM courses", conn)
    enroll = pd.read_sql("SELECT * FROM enrollments", conn, parse_dates=["EnrollDate"])

    # Join tables
    df = enroll.merge(students, on="StudentID").merge(courses, on="CourseID")

    # Calculated fields
    df['CompletionStatus'] = df['Progress'].apply(lambda x: 'Completed' if x >= 80 else 'In Progress')
    df['EnrollMonth'] = df['EnrollDate'].dt.to_period('M').astype(str)

    # Save processed file
    df.to_csv("data/processed_enrollments.csv", index=False)
    conn.close()
    print("Processed enrollments saved!")


if __name__ == "__main__":
    process_enrollments()
