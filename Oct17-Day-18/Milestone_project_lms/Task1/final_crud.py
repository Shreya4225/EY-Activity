import pandas as pd

courses = pd.read_csv("../courses.csv")
students = pd.read_csv("../students.csv")

# Add a new course
new_course = {"CourseID": "C105", "Title": "Deep Learning", "Category": "AI", "Duration": 70}
courses = pd.concat([courses, pd.DataFrame([new_course])], ignore_index=True)
print("After adding new course:")
print(courses)

# Update course duration
courses.loc[courses["CourseID"] == "C101", "Duration"] = 45
print("\nAfter updating duration of C101:")
print(courses)

# Delete a student
students = students.drop(students[students["StudentID"] == "S004"].index)
print("\nAfter deleting student S004:")
print(students)

# Fetch all students from India
indian_students = students[students["Country"] == "India"]
print("\nStudents from India:")
print(indian_students)


