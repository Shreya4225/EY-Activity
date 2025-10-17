import pandas as pd
import sqlite3
import logging
import time
from pathlib import Path

# -----------------------------
# Setup logging configuration
# -----------------------------
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)
LOG_FILE = LOGS_DIR / "lms.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DB = "lms.db"


# -----------------------------
# ETL with logging and error handling
# -----------------------------
def etl_with_logging():
    start_time = time.perf_counter()
    logging.info("ETL process started.")

    try:
        conn = sqlite3.connect(DB)
        students = pd.read_sql("SELECT * FROM students", conn)
        courses = pd.read_sql("SELECT * FROM courses", conn)
        enrollments = pd.read_sql("SELECT * FROM enrollments", conn, parse_dates=["EnrollDate"])

        # Check for missing student or course references
        missing_students = enrollments[~enrollments["StudentID"].isin(students["StudentID"])]
        missing_courses = enrollments[~enrollments["CourseID"].isin(courses["CourseID"])]

        for _, row in missing_students.iterrows():
            logging.error(f"Missing student: {row['StudentID']} in enrollment {row['EnrollmentID']}")
        for _, row in missing_courses.iterrows():
            logging.error(f"Missing course: {row['CourseID']} in enrollment {row['EnrollmentID']}")

        # Process only valid enrollments
        valid_enrollments = enrollments[
            enrollments["StudentID"].isin(students["StudentID"]) &
            enrollments["CourseID"].isin(courses["CourseID"])
            ]

        # Join with student & course data
        df = valid_enrollments.merge(students, on="StudentID").merge(courses, on="CourseID")

        # Add calculated fields
        df["CompletionStatus"] = df["Progress"].apply(lambda x: "Completed" if x >= 80 else "In Progress")
        df["EnrollMonth"] = df["EnrollDate"].dt.to_period("M").astype(str)

        # Save processed file
        df.to_csv("data/processed_enrollments.csv", index=False)

        # Log each new enrollment
        for _, row in df.iterrows():
            logging.info(
                f"New enrollment processed: {row['EnrollmentID']} - Student: {row['StudentID']} - "
                f"Course: {row['CourseID']} - Status: {row['CompletionStatus']}"
            )

        runtime = round(time.perf_counter() - start_time, 2)
        logging.info(f"ETL completed successfully in {runtime} seconds.")
        print("ETL completed successfully.")

    except Exception as e:
        logging.error(f"ETL failed: {e}")
        print("ETL failed. Check logs for details.")

    finally:
        conn.close()


# -----------------------------
# Run directly
# -----------------------------
if __name__ == "__main__":
    etl_with_logging()
