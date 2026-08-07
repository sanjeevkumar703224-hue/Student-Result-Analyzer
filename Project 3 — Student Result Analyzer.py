#Project 3 — Student Result Analyzer
import 
import os

FILE_NAME = "students.json"

students = []

subjects = [
    "Python",
    "DSA",
    "DBMS",
    "OS",
    "Maths"
]


def load_data():
    global students

    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                students = json.load(file)
        except:
            students = []


def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def calculate_total(marks):
    return sum(marks.values())


def calculate_percentage(marks):
    total = calculate_total(marks)
    return total / len(subjects)


def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


def get_status(marks):
    for mark in marks.values():
        if mark < 35:
            return "FAIL"
    return "PASS"


def add_student():
    print("\n========== ADD STUDENT ==========")

    name = input("Enter student name: ").strip()

    if not name:
        print("Invalid name!")
        return

    for student in students:
        if student["name"].lower() == name.lower():
            print("Student already exists!")
            return

    marks = {}

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter {subject} marks: "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Enter a valid number.")

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)
    save_data()

    print("\nStudent added successfully!")


def view_students():
    print("\n========== ALL STUDENTS ==========")

    if not students:
        print("No students found.")
        return

    for i, student in enumerate(students, 1):
        total = calculate_total(student["marks"])
        percentage = calculate_percentage(student["marks"])
        grade = get_grade(percentage)
        status = get_status(student["marks"])

        print(f"""
{i}. {student["name"]}
--------------------------------
Python : {student["marks"]["Python"]}
DSA    : {student["marks"]["DSA"]}
DBMS   : {student["marks"]["DBMS"]}
OS     : {student["marks"]["OS"]}
Maths  : {student["marks"]["Maths"]}

Total      : {total}/500
Percentage : {percentage:.2f}%
Grade      : {grade}
Status     : {status}
""")


def student_report():
    print("\n========== STUDENT REPORT ==========")

    name = input("Enter student name: ").strip()

    for student in students:
        if student["name"].lower() == name.lower():

            marks = student["marks"]
            total = calculate_total(marks)
            percentage = calculate_percentage(marks)
            grade = get_grade(percentage)
            status = get_status(marks)

            highest_subject = max(marks, key=marks.get)
            lowest_subject = min(marks, key=marks.get)

            print("""
========================================
          STUDENT RESULT
========================================
""")

            print(f"Student: {student['name']}")
            print("----------------------------------------")

            for subject in subjects:
                print(f"{subject:<10}: {marks[subject]}")

            print("----------------------------------------")
            print(f"Total       : {total}/500")
            print(f"Percentage  : {percentage:.2f}%")
            print(f"Grade       : {grade}")
            print(f"Status      : {status}")
            print(f"Highest     : {highest_subject} ({marks[highest_subject]})")
            print(f"Lowest      : {lowest_subject} ({marks[lowest_subject]})")

            print("========================================")

            return

    print("Student not found.")


def find_topper():
    print("\n========== CLASS TOPPER ==========")

    if not students:
        print("No students found.")
        return

    topper = max(
        students,
        key=lambda student: calculate_percentage(student["marks"])
    )

    percentage = calculate_percentage(topper["marks"])
    total = calculate_total(topper["marks"])
    grade = get_grade(percentage)

    print(f"Name       : {topper['name']}")
    print(f"Total      : {total}/500")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")


def subject_analysis():
    print("\n========== SUBJECT ANALYSIS ==========")

    if not students:
        print("No students found.")
        return

    for subject in subjects:
        highest = max(
            students,
            key=lambda student: student["marks"][subject]
        )

        lowest = min(
            students,
            key=lambda student: student["marks"][subject]
        )

        average = sum(
            student["marks"][subject]
            for student in students
        ) / len(students)

        print(f"""
{subject}
--------------------------------
Average : {average:.2f}
Highest : {highest['name']} ({highest['marks'][subject]})
Lowest  : {lowest['name']} ({lowest['marks'][subject]})
""")


def class_statistics():
    print("\n========== CLASS STATISTICS ==========")

    if not students:
        print("No students found.")
        return

    percentages = [
        calculate_percentage(student["marks"])
        for student in students
    ]

    class_average = sum(percentages) / len(percentages)

    passed = sum(
        1 for student in students
        if get_status(student["marks"]) == "PASS"
    )

    failed = len(students) - passed

    pass_percentage = (passed / len(students)) * 100

    highest = max(percentages)
    lowest = min(percentages)

    print(f"Total Students : {len(students)}")
    print(f"Class Average  : {class_average:.2f}%")
    print(f"Highest        : {highest:.2f}%")
    print(f"Lowest         : {lowest:.2f}%")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")
    print(f"Pass Percentage: {pass_percentage:.2f}%")

    print("======================================")


def search_student():
    print("\n========== SEARCH STUDENT ==========")

    name = input("Enter student name: ").strip().lower()

    found = False

    for student in students:
        if name in student["name"].lower():

            percentage = calculate_percentage(student["marks"])
            total = calculate_total(student["marks"])

            print(
                f"\nName: {student['name']}"
                f"\nTotal: {total}/500"
                f"\nPercentage: {percentage:.2f}%"
                f"\nGrade: {get_grade(percentage)}"
                f"\nStatus: {get_status(student['marks'])}"
            )

            found = True

    if not found:
        print("No student found.")


def delete_student():
    print("\n========== DELETE STUDENT ==========")

    if not students:
        print("No students found.")
        return

    name = input("Enter student name: ").strip()

    for i, student in enumerate(students):

        if student["name"].lower() == name.lower():

            students.pop(i)
            save_data()

            print("Student deleted successfully!")
            return

    print("Student not found.")


def clear_students():
    global students

    print("\n========== CLEAR ALL DATA ==========")

    if not students:
        print("No data found.")
        return

    confirmation = input(
        "Delete all student records? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        students = []
        save_data()
        print("All student records deleted.")
    else:
        print("Operation cancelled.")


def show_menu():
    print("""
========================================
       🎓 STUDENT RESULT ANALYZER
========================================

1. Add Student
2. View All Students
3. Student Report
4. Find Class Topper
5. Subject Analysis
6. Class Statistics
7. Search Student
8. Delete Student
9. Clear All Students
10. Exit

========================================
""")


def main():
    load_data()

    print("""
========================================
     WELCOME TO STUDENT RESULT ANALYZER
========================================
""")

    while True:

        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            student_report()

        elif choice == "4":
            find_topper()

        elif choice == "5":
            subject_analysis()

        elif choice == "6":
            class_statistics()

        elif choice == "7":
            search_student()

        elif choice == "8":
            delete_student()

        elif choice == "9":
            clear_students()

        elif choice == "10":
            save_data()
            print("\nThank you for using Student Result Analyzer!")
            break

        else:
            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    main()
