import queue
import threading
import pandas as pd
import sqlite3
import logging
from pathlib import Path
import time

# Setup logs
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)
LOG_FILE = LOGS_DIR / "lms.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

DB = "lms.db"
q = queue.Queue()


# Producer: pushes new enrollment records into the queue
def producer(new_enrollments):
    for enrollment in new_enrollments:
        q.put(enrollment)
        logging.info(f"Enrollment pushed to queue: {enrollment['EnrollmentID']}")
    print(f"{len(new_enrollments)} enrollments pushed to queue.")


# Consumer: processes enrollments from the queue
def consumer():
    conn = sqlite3.connect(DB)
    processed_count = 0

    # Load existing processed enrollments
    try:
        df_processed = pd.read_csv("data/processed_enrollments.csv", parse_dates=["EnrollDate"])
    except FileNotFoundError:
        df_processed = pd.DataFrame()

    while not q.empty():
        enrollment = q.get()

        # Check student & course exist
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM students WHERE StudentID=?", (enrollment["StudentID"],))
        student_exists = cur.fetchone()[0] > 0
        cur.execute("SELECT COUNT(*) FROM courses WHERE CourseID=?", (enrollment["CourseID"],))
        course_exists = cur.fetchone()[0] > 0

        if student_exists and course_exists:
            # Add calculated fields
            enrollment["CompletionStatus"] = "Completed" if enrollment["Progress"] >= 80 else "In Progress"
            #["EnrollMonth"] = pd.to_datetime(enrollment["EnrollDate"]).to_period("M").astype(str)
            enrollment["EnrollMonth"] = str(pd.to_datetime(enrollment["EnrollDate"]).to_period("M"))

            # Append to processed DataFrame
            df_processed = pd.concat([df_processed, pd.DataFrame([enrollment])], ignore_index=True)
            processed_count += 1
        else:
            logging.error(f"Missing student or course for enrollment {enrollment['EnrollmentID']}")

    # Save updated processed enrollments
    df_processed.to_csv("data/processed_enrollments.csv", index=False)
    conn.close()
    logging.info(f"Consumer processed {processed_count} enrollments.")
    print(f"Consumer processed {processed_count} enrollments.")


# -----------------------
# Example usage
if __name__ == "__main__":
    new_enrollments = [
        {"EnrollmentID": "E007", "StudentID": "S001", "CourseID": "C102", "EnrollDate": "2025-10-07", "Progress": 90},
        #{"EnrollmentID": "E008", "StudentID": "S002", "CourseID": "C103", "EnrollDate": "2025-10-08", "Progress": 70}
    ]

    producer(new_enrollments)
    consumer()
