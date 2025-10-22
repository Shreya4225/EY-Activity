import pandas as pd
from datetime import datetime
import logging
import schedule
import time

logging.basicConfig(
    filename='daily_report.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def generate_daily_report():
    students_df = pd.read_csv("../students.csv")
    courses_df = pd.read_csv("../courses.csv")
    enrollments_df = pd.read_csv("../enrollments.csv")

    df = enrollments_df.merge(students_df, on="StudentID", how="left")
    df = df.merge(courses_df, on="CourseID", how="left")
    df['CompletionStatus'] = df['Progress'].apply(lambda x: "Completed" if x >= 80 else "In Progress")
    df['EnrollMonth'] = pd.to_datetime(df['EnrollDate']).dt.month

    today = datetime.today().strftime('%Y%m%d')
    report_file = f'daily_enrollment_report_{today}.csv'
    df.to_csv(report_file, index=False)
    logging.info(f"Daily report generated: {report_file}")
    print(f"Report generated: {report_file}")

# Schedule the job every day at 9:00 AM
schedule.every().day.at("09:00").do(generate_daily_report)

print("Scheduler started. Waiting for 9:00 AM...")

while True:
    schedule.run_pending()
    time.sleep(60)


# import pandas as pd
# from datetime import datetime
# import logging
#
# logging.basicConfig(
#     filename='daily_report.log',
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )
#
# # Load CSVs
# students_df = pd.read_csv("../students.csv")
# courses_df = pd.read_csv("../courses.csv")
# enrollments_df = pd.read_csv("../enrollments.csv")
#
# # Generate report
# df = enrollments_df.merge(students_df, on="StudentID", how="left")
# df = df.merge(courses_df, on="CourseID", how="left")
# df['CompletionStatus'] = df['Progress'].apply(lambda x: "Completed" if x >= 80 else "In Progress")
# df['EnrollMonth'] = pd.to_datetime(df['EnrollDate']).dt.month
#
# today = datetime.today().strftime('%Y%m%d') #Formats the date into a string in the pattern 2025/10/19
# report_file = f'daily_enrollment_report_{today}.csv'
# df.to_csv(report_file, index=False)
# logging.info(f"Daily report generated: {report_file}")
