import sqlite3

DB = "lms.db"

# --- Courses ---
def add_course(course):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO courses VALUES (?,?,?,?)",
                (course['CourseID'], course['Title'], course['Category'], course['Duration']))
    conn.commit()
    conn.close()

def update_course_duration(course_id, duration):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("UPDATE courses SET Duration=? WHERE CourseID=?", (duration, course_id))
    conn.commit()
    conn.close()

def delete_course(course_id):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("DELETE FROM courses WHERE CourseID=?", (course_id,))
    conn.commit()
    conn.close()

# --- Students ---
def add_student(student):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO students VALUES (?,?,?,?)",
                (student['StudentID'], student['Name'], student['Email'], student['Country']))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE StudentID=?", (student_id,))
    conn.commit()
    conn.close()

def fetch_students_from(country):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE Country=?", (country,))
    rows = cur.fetchall()
    conn.close()
    return rows

# --- Example ---
if __name__ == "__main__":
    # add_course({'CourseID':'C106','Title':'AI Basics','Category':'AI','Duration':45})
     update_course_duration('C106', 100)
    # delete_student('S005')
     print(fetch_students_from("India"))
