import pandas as pd
import logging
import time

# Logging setup
logging.basicConfig(
    filename="Task5\enrollment_etl.log",  # log file location
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load CSVs
students = pd.read_csv("students.csv")
courses = pd.read_csv("courses.csv")

try:
    processed_df = pd.read_csv("processed_enrollments.csv")
except FileNotFoundError:
    processed_df = pd.DataFrame()


# Process a list of new enrollments
def process_enrollments(new_enrollments):
    global processed_df
    start_time = time.time()
    processed_count = 0

    for enrollment in new_enrollments:
        enrollment_id = enrollment.get("EnrollmentID", "Unknown")
        logging.info(f"New enrollment received: {enrollment_id}")
        try:
            # Validate student
            if enrollment["StudentID"] not in students["StudentID"].values:
                raise ValueError(f"StudentID {enrollment['StudentID']} not found")
            # Validate course
            if enrollment["CourseID"] not in courses["CourseID"].values:
                raise ValueError(f"CourseID {enrollment['CourseID']} not found")

            # ETL processing
            df = pd.DataFrame([enrollment])
            df = df.merge(students, on="StudentID", how="left")
            df = df.merge(courses, on="CourseID", how="left")
            df["CompletionStatus"] = df["Progress"].apply(lambda x: "Completed" if x >= 80 else "In Progress")
            df["EnrollMonth"] = pd.to_datetime(df["EnrollDate"]).dt.month

            # Append to processed_df
            processed_df = pd.concat([processed_df, df], ignore_index=True)
            processed_count += 1
            logging.info(f"Enrollment {enrollment_id} processed successfully")

        except Exception as e:
            logging.error(f"Error processing enrollment {enrollment_id}: {e}")

    # Save processed enrollments
    processed_df.to_csv("processed_enrollments.csv", index=False)

    runtime = round(time.time() - start_time, 2)
    logging.info(f"ETL completed: {processed_count} records processed in {runtime} seconds")
    print(f"ETL completed: {processed_count} records processed in {runtime} seconds")


# Example usage
new_enrollments = [
    {"EnrollmentID": "E011", "StudentID": "S001", "CourseID": "C101", "EnrollDate": "2025-10-11", "Progress": 90},
    {"EnrollmentID": "E012", "StudentID": "S999", "CourseID": "C103", "EnrollDate": "2025-10-12", "Progress": 50},
    # invalid student
]

process_enrollments(new_enrollments)
