students = []


def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    student = {
        "id": len(students) + 1,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No students found.\n")
        return

    print("\n--- Student List ---")

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Course: {student['course']}"
        )

    print()


def search_student():
    name = input("Enter student name: ")
    found = False

    for student in students:
        if name.lower() in student["name"].lower():
            print(
                f"ID: {student['id']} | "
                f"Name: {student['name']} | "
                f"Age: {student['age']} | "
                f"Course: {student['course']}"
            )
            found = True

    if not found:
        print("Student not found.")

    print()


def update_student():
    student_id = int(input("Enter student ID to update: "))

    for student in students:
        if student["id"] == student_id:
            print("\nLeave a field empty to keep the old value.")

            name = input(f"New name ({student['name']}): ")
            age = input(f"New age ({student['age']}): ")
            course = input(f"New course ({student['course']}): ")

            if name:
                student["name"] = name

            if age:
                student["age"] = age

            if course:
                student["course"] = course

            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


while True:
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.\n")