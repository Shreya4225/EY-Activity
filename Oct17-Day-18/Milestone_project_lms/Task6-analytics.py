import pandas as pd
import os

# -----------------------------
# Create reports folder if it doesn't exist
# -----------------------------
if not os.path.exists("reports"):
    os.makedirs("reports")

# -----------------------------
# Load processed enrollments
# -----------------------------
df = pd.read_csv("processed_enrollments.csv", parse_dates=["EnrollDate"])

# -----------------------------
# 1. Completion rate per course
# -----------------------------
completion_rate = df.groupby("CourseID")["CompletionStatus"].apply(lambda x: (x=="Completed").mean()).reset_index(name="CompletionRate")

# -----------------------------
# 2. Total students per category
# -----------------------------
students_per_category = df.groupby("Category")["StudentID"].nunique().reset_index(name="TotalStudents")

# -----------------------------
# 3. Country-wise enrollments
# -----------------------------
country_wise = df.groupby("Country").size().reset_index(name="Enrollments")

# -----------------------------
# 4. Monthly enrollment trends
# -----------------------------
df["EnrollMonth"] = pd.to_datetime(df["EnrollDate"]).dt.month
monthly = df.groupby("EnrollMonth").size().reset_index(name="Enrollments")

# -----------------------------
# Save reports as separate CSV files
# -----------------------------
completion_rate.to_csv("reports/completion_rate.csv", index=False)
students_per_category.to_csv("reports/students_per_category.csv", index=False)
country_wise.to_csv("reports/country_enrollments.csv", index=False)
monthly.to_csv("reports/monthly_enrollments.csv", index=False)

print("Analytics reports generated!")
