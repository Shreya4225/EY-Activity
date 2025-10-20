import pandas as pd

#Load CSV files into DataFrames
courses_file = '../courses.csv'
students_file = '../students.csv'

courses_df = pd.read_csv(courses_file)
students_df = pd.read_csv(students_file)

# Define CRUD functions
def add_course():
    course_id = input("Enter CourseID: ")
    title = input("Enter Title: ")
    category = input("Enter Category: ")
    duration = int(input("Enter Duration (hours): "))
    global courses_df
    courses_df = pd.concat([courses_df, pd.DataFrame([{
        'CourseID': course_id,
        'Title': title,
        'Category': category,
        'Duration': duration
    }])], ignore_index=True)
    print("Course added successfully!")

def update_course_duration():
    course_id = input("Enter CourseID to update: ")
    new_duration = int(input("Enter new Duration: "))
    global courses_df
    if course_id in courses_df['CourseID'].values:
        courses_df.loc[courses_df['CourseID'] == course_id, 'Duration'] = new_duration
        print("Duration updated successfully!")
    else:
        print("CourseID not found.")

def delete_student():
    student_id = input("Enter StudentID to delete: ")
    global students_df
    if student_id in students_df['StudentID'].values:
        students_df = students_df[students_df['StudentID'] != student_id]
        print("Student deleted successfully!")
    else:
        print("StudentID not found.")

def fetch_students_from_india():
    india_students = students_df[students_df['Country'] == 'India']
    print("\nStudents from India:")
    print(india_students)

def display_courses():
    print("\nCourses Table:")
    print(courses_df)

def display_students():
    print("\nStudents Table:")
    print(students_df)

#  Main loop for user actions
while True:
    print("\nChoose an action:")
    print("1. Add a new course")
    print("2. Update course duration")
    print("3. Delete a student")
    print("4. Fetch all students from India")
    print("5. Show all courses")
    print("6. Show all students")
    print("0. Exit")

    choice = input("Enter choice (0-6): ")

    if choice == '1':
        add_course()
    elif choice == '2':
        update_course_duration()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        fetch_students_from_india()
    elif choice == '5':
        display_courses()
    elif choice == '6':
        display_students()
    elif choice == '0':
        # Save changes back to CSV before exit
        courses_df.to_csv(courses_file, index=False)
        students_df.to_csv(students_file, index=False)
        print("Changes saved. Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
