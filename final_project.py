"""
ITF 07 Final Project Attendance System
Name : Adel Akram Madi
Delivery Date :
"""
from uuid import uuid4


class Course:
    def __init__(self, name, mark):
        self.course_id = uuid4()
        self.name = name
        self.mark = mark


class Student:
    total_count = 0

    def __init__(self, student_name, student_age, student_number):
        self.student_id = uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total_count += 1

    def enroll_course(self, course):
        self.courses_list.append(course)

    def get_student_details(self):
        return self.__dict__

    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course: {course.name}, Mark: {course.mark}")

    def get_student_average(self):
        if not self.courses_list:
            return 0
        total_marks = sum(course.mark for course in self.courses_list)
        return total_marks / len(self.courses_list)


students = []

while True:
    try:
        selection = int(input("1. Add New Student\n"
                              "2. Delete Student\n"
                              "3. Display Student\n"
                              "4.Add Course to Student with Mark \n"
                              "5. Get Student Average\n"
                              "6. Exit \n"))

                             


        if selection == 1:
            student_number = input("Enter Student Number: ")
            if any(student.student_number == student_number for student in students):
                print("Student Number already exists.")
                continue

            student_name = input("Enter Student Name: ")
            while True:
                try:
                    student_age = int(input("Enter Student Age: "))
                    break
                except ValueError:
                    print("Invalid Value")

            student = Student(student_name, student_age, student_number)
            students.append(student)
            print("Student Added Successfully")

        elif selection == 2:
            student_number = input("Enter Student Number: ")
            for student in students:
                if student.student_number == student_number:
                    students.remove(student)
                    print("Student Deleted Successfully")
                    break
            else:
                print("Student Not Exist")

        elif selection == 3:
            student_number = input("Enter Student Number: ")
            for student in students:
                if student.student_number == student_number:
                    print("Student Details:")
                    print(f"Name: {student.student_name}")
                    print(f"Age: {student.student_age}")
                    print(f"Number: {student.student_number}")
                    print("Courses:")
                    student.get_student_courses()
                    break
            else:
                print("Student Not Exist")
        elif selection == 4:
            student_number = input("Enter Student Number: ")
            for student in students:
                if student.student_number == student_number:
                    course_name = input("Enter Course Name: ")
                    course_mark = int(input("Enter Course Mark: "))
                    course = Course(course_name, course_mark)
                    student.enroll_course(course)
                    print("Course Added Successfully")
                    break
            else:
                print("Student Not Exist")

        elif selection ==5:
            student_number = input("Enter Student Number: ")
            for student in students:
                if student.student_number == student_number:
                    average = student.get_student_average()
                    print(f"Student Average: {average}")
                    break
            else:
                print("Student Not Exist")

        elif selection == 6:
            print("Exiting the program...")
            exit()

    except ValueError:
        print("Invalid selection. Please enter a valid option.")
