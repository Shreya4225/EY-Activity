import pandas as pd
import queue
import threading
import logging
import time

# -----------------------------
# Logging setup
# -----------------------------
logging.basicConfig(
    filename="Task4\enrollment_processing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------
# In-memory queue
# -----------------------------
enrollment_queue = queue.Queue()

# -----------------------------
# Load CSVs
# -----------------------------
students = pd.read_csv("students.csv")
courses = pd.read_csv("courses.csv")

try:
    processed_df = pd.read_csv("processed_enrollments.csv")
except FileNotFoundError:
    processed_df = pd.DataFrame()

# -----------------------------
# Global counter
# -----------------------------
processed_count = 0


# -----------------------------
# Producer function
# -----------------------------
def producer(new_enrollments):
    for record in new_enrollments:
        enrollment_queue.put(record)
        logging.info(f"Produced enrollment: {record['EnrollmentID']}")


# -----------------------------
# Consumer function
# -----------------------------
def consumer():
    global processed_df, processed_count
    start_time = time.time()

    while not enrollment_queue.empty():
        record = enrollment_queue.get()
        enrollment_id = record.get("EnrollmentID", "Unknown")
        try:
            # Validate student and course
            if record["StudentID"] not in students["StudentID"].values:
                raise ValueError(f"StudentID {record['StudentID']} not found")
            if record["CourseID"] not in courses["CourseID"].values:
                raise ValueError(f"CourseID {record['CourseID']} not found")

            # ETL processing
            df = pd.DataFrame([record])
            df = df.merge(students, on="StudentID", how="left")
            df = df.merge(courses, on="CourseID", how="left")
            df["CompletionStatus"] = df["Progress"].apply(lambda x: "Completed" if x >= 80 else "In Progress")
            df["EnrollMonth"] = pd.to_datetime(df["EnrollDate"]).dt.month

            # Append to processed_df
            processed_df = pd.concat([processed_df, df], ignore_index=True)
            processed_count += 1
            logging.info(f"Processed enrollment: {enrollment_id} successfully")
        except Exception as e:
            logging.error(f"Error processing enrollment {enrollment_id}: {e}")
        finally:
            enrollment_queue.task_done()

    # Save processed CSV
    processed_df.to_csv("processed_enrollments.csv", index=False)
    runtime = round(time.time() - start_time, 2)
    logging.info(f"ETL completed: {processed_count} records processed in {runtime} seconds")
    print(f"ETL completed: {processed_count} records processed")


# -----------------------------
# Example usage
# -----------------------------
new_enrollments = [
    {"EnrollmentID": "E011", "StudentID": "S001", "CourseID": "C101", "EnrollDate": "2025-10-11", "Progress": 90},
    {"EnrollmentID": "E012", "StudentID": "S003", "CourseID": "C103", "EnrollDate": "2025-10-12", "Progress": 50},
]

# Start producer thread
producer_thread = threading.Thread(target=producer, args=(new_enrollments,))
producer_thread.start()
producer_thread.join()

# Start consumer thread
consumer_thread = threading.Thread(target=consumer)
consumer_thread.start()
consumer_thread.join()
