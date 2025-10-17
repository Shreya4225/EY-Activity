import pandas as pd

# -----------------------------
# 1️⃣ Load CSV files
# -----------------------------
students = pd.read_csv("students.csv")
courses = pd.read_csv("courses.csv")
enrollments = pd.read_csv("enrollments.csv")

# -----------------------------
# 2️⃣ Join tables
# -----------------------------
# Merge enrollments with students
df = enrollments.merge(students, on="StudentID", how="left")
# Merge the result with courses
df = df.merge(courses, on="CourseID", how="left")

# -----------------------------
# 3️⃣ Add calculated fields
# -----------------------------
# CompletionStatus: Completed if Progress >= 80
df["CompletionStatus"] = df["Progress"].apply(lambda x: "Completed" if x >= 80 else "In Progress")

# EnrollMonth: extract month from EnrollDate
df["EnrollMonth"] = pd.to_datetime(df["EnrollDate"]).dt.month

# -----------------------------
# 4️⃣ Save processed data
# -----------------------------
df.to_csv("processed_enrollments.csv", index=False)

print("Processed enrollments saved as 'processed_enrollments.csv'")
