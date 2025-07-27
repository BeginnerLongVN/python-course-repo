from student_object import Student
from subject_object import Subject
import json 
import csv 
import os

def show_menu(): 
    print("="*40+ "\n")
    print("STUDENT MANAGEMENT SYSTEM".center(40)+ "\n")
    print("="*40+ "\n")
    print("1. Add New Student")
    print("2. Add Course with Grade to Student")
    print("3. View Student List")
    print("4. View Student Transcript")
    print("5. Export Student Transcript to TXT")
    print("6. Remove Course from Student")
    print("7. Show Top Students by GPA")
    print("8. Filter Students by Minimum GPA")
    print("9. Export Class Summary")
    print("10. Import Students from CSV")
    print("11. Exit")
    print("-"*40+ "\n")


def add_new_student(students_list):
    student_id = input(">>Enter Student ID: ")
    student_name = input(">>Enter Student Name: ")
    student = Student(student_id, student_name)
    students_list.append(student)
    print(f"Student {student_name} added successfully!")

def add_course_course_to_student(students_list):
    id = input("\n>>Enter Student ID: ")
    course_name = input(">>Enter Course Name: ")
    grade = input(">>Enter score(0-10):")
    print(f"Course {course_name} with score {grade} added to student with ID {id}.")
    for student in students_list: 
        if student.get_id() == id:
            subject = Subject(course_name, grade)
            student.add_subject_with_grade(subject)
            return
        
    print(f"No student found with ID {id}. ")

def view_student_list(students_list):
    print('\n' + "List of students: ".center(40, "-") )
    for student in students_list:
        student.show_info()

def view_student_transcript(students_list):
    id = input("\n>>Enter Student ID: ")
    for student in students_list:
        if student.get_id() == id: 
            print('\n' + f"Transcript for {student.get_id()} - {student.get_name()}:".center(40, "-"))
            for subject in student.subjects:
                print(f"Course: {subject.get_subject()} | Score: {subject.get_score()}")
            print(f"GPA: {student.get_gpa():.2f}")
            return

    print(f"No student found with ID {id}.")

def transcript_to_txt(students_list):
    id = input("\n>>Enter Student ID:")
    for student in students_list: 
        if student.get_id() == id: 
            with open("student_info.txt", "w") as file: 
                file.write("Academic Transcript".center(40, "=") + "\n")
                file.write(f"Student ID: {student.get_id()}\n")
                file.write(f"Student name: {student.get_name()}\n")
                file.write(f"Courses:\n")
                for subject in student.subjects: 
                    file.write(f"- {subject.get_subject()}: {subject.get_score()}\n\n")
                file.write(f"GPA: {student.get_gpa():.2f}\n")


def remove_course_from_student(students_list):
    id = input("\n>>Enter student ID: ")
    course_name = input("\n>>Enter course name to remove: ")
    for student in students_list: 
        if student.get_id() == id: 
            student.remove_subject(course_name)

def show_top_students_by_gpa(students_list):
    number = int(input("\n>>Enter N (e.g. 3): "))
    sorted_students = sorted(students_list, key = lambda student: student.get_gpa(), reverse=True)
    print(f"\nTop {number} students by GPA".center(40, "-"))
    for student in sorted_students[:number]:
        student.show_info()
    print("\n")

def filter_students_by_minimum_gpa(students_list):
    min_gpa = float(input("\n>>Enter minimum GPA: "))
    print(f"\nStudents with GPA >= {min_gpa}".center(40, "-"))
    for student in students_list: 
        if student.get_gpa() >= min_gpa: 
            student.show_info()
    

def export_class_summary(students_list):
    highest_student = max(students_list, key = lambda student: student.get_gpa())
    lowest_student = min(students_list, key = lambda student: student.get_gpa())
    average_gpa = sum(students_list, key = lambda student: student.get_gpa()) / len(students_list)
    with open("class_summary.txt", "w") as file: 
        file.write("Class Summary Report".center(40, "=") + "\n")
        file.write(f"Total Students: {len(students_list)}\n\n")
        file.write(f"Average GPA: {average_gpa:.2f}\n")
        file.write(f"Highest GPA: {highest_student.get_gpa():.2f} ({highest_student.get_name()} - {highest_student.get_id()})\n" )
        file.write(f"Lowest GPA: {lowest_student.get_gpa():.2f} ({lowest_student.get_name()} - {lowest_student.get_id()})\n")
        
    



def import_students_from_csv(students_list, file_name):
    if not os.path.exists(file_name):
        print(f"File {file_name} does not exist.")
        return 
    
    with open(file_name, newline='', encoding = 'utf-8') as file: 
        data_dict = file.DictReader(file)
        for row in data_dict: 
            
    

def save_students_to_json(students_list):
    with open("students.json", "w") as file: 
        json.dump([Student.to_dict(student) for student in students_list], file, indent=4)
        

def load_students_from_json():
    if os.path.exists("students.json") and os.path.getsize("students.json") > 0: 
        with open("students.json", "r") as file: 
            data = json.load(file)
            return [Student.from_dict(student_data) for student_data in data]
    else: 
        return []

def main(): 
    students_list = load_students_from_json()
    show_menu()
    while True:
        choice = input("Select an option (1-11): ")
        if choice == '1':
            add_new_student(students_list)
        elif choice == '2':
            add_course_course_to_student(students_list)
        elif choice == '3':     
            view_student_list(students_list)
        elif choice == '4':
            view_student_transcript(students_list)
        elif choice == '5':
            transcript_to_txt(students_list)
        elif choice == '6': 
            remove_course_from_student(students_list)
        elif choice == '7':
            show_top_students_by_gpa(students_list)
        elif choice == '8':
            filter_students_by_minimum_gpa(students_list)
        elif choice == '9':
            export_class_summary(students_list)
        elif choice == '10':
            file_name = input(">>Enter CSV file name to import: ")
            import_students_from_csv(students_list, file_name)
        elif choice == '11':
            print("Exiting the Student Management System. Goodbye!")
            save_students_to_json(students_list)
            break

if __name__ == "__main__":
    main()

