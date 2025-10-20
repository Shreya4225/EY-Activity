import pandas as pd

#  Load CSV files
students = pd.read_csv("students.csv")
courses = pd.read_csv("courses.csv")
enrollments = pd.read_csv("enrollments.csv")

# Merge enrollments with students
# In ETL/reporting, we often want all enrollments, even if the data is incomplete, so we can log errors or handle missing data.
df = enrollments.merge(students, on="StudentID", how="left")
# Merge the result with courses
df = df.merge(courses, on="CourseID", how="left")

# Completed if Progress >= 80
df["CompletionStatus"] = df["Progress"].apply(lambda x: "Completed" if x >= 80 else "In Progress")

# Extract month from EnrollDate
df["EnrollMonth"] = pd.to_datetime(df["EnrollDate"]).dt.month

#  Save processed data
df.to_csv("processed_enrollments.csv", index=False)

print("Processed enrollments saved as 'processed_enrollments.csv'")
