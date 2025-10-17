import pandas as pd

df = pd.read_csv("data/processed_enrollments.csv", parse_dates=["EnrollDate"])

# Completion rate per course
completion_rate = df.groupby("CourseID")["CompletionStatus"].apply(lambda x: (x=="Completed").mean()).reset_index(name="CompletionRate")

# Total students per category
students_per_category = df.groupby("Category")["StudentID"].nunique().reset_index(name="TotalStudents")

# Country-wise enrollments
country_wise = df.groupby("Country").size().reset_index(name="Enrollments")

# Monthly trends
monthly = df.groupby("EnrollMonth").size().reset_index(name="Enrollments")

# Save reports
completion_rate.to_csv("reports/completion_rate.csv", index=False)
students_per_category.to_csv("reports/students_per_category.csv", index=False)
country_wise.to_csv("reports/country_enrollments.csv", index=False)
monthly.to_csv("reports/monthly_enrollments.csv", index=False)

print("Analytics reports generated!")
