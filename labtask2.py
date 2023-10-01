students = {
    "001": {"Name": "Husnain", "Email": "fa20-bce-001@cuilahore.edu.pk", "Gender": "Male"},
    "002": {"Name": "Tahla", "Email": "fa20-bce-002@cuilahore.edu.pk", "Gender": "Male"},
    "003": {"Name": "Hamid", "Email": "fa20-bce-003@cuilahore.edu.pk", "Gender": "Male"},
    "004": {"Name": "Alice", "Email": "fa20-bce-004@cuilahore.edu.pk", "Gender": "Female"}
}

def add_student():
    reg_number = input("Enter student's registration number: ")
    name = input("Enter student's name: ")
    email = input("Enter student's email: ")
    gender = input("Enter student's gender: ")

    student_info = {"Name": name, "Email": email, "Gender": gender}
    students[reg_number] = student_info
    print("Student record added successfully!")

def delete_student():
    reg_number = input("Enter the registration number of the student to delete: ")
    if reg_number in students:
        del students[reg_number]
        print("Student record deleted successfully!")
    else:
        print("Student not found!")

def update_student():
    reg_number = input("Enter the registration number of the student to update: ")
    if reg_number in students:
        name = input("Enter updated name: ")
        email = input("Enter updated email: ")
        gender = input("Enter updated gender: ")

        students[reg_number]["Name"] = name
        students[reg_number]["Email"] = email
        students[reg_number]["Gender"] = gender
        print("Student record updated successfully!")
    else:
        print("Student not found!")

def view_student():
    reg_number = input("Enter the registration number of the student to view details: ")
    if reg_number in students:
        student_info = students[reg_number]
        print(f"Registration Number: {reg_number}")
        print(f"Name: {student_info['Name']}")
        print(f"Email: {student_info['Email']}")
        print(f"Gender: {student_info['Gender']}")
    else:
        print("Student not found!")

def list_students():
    if not students:
        print("No student records found.")
    else:
        print("Student Records:")
        for reg_number, student_info in students.items():
            print(f"Registration Number: {reg_number}")
            print(f"Name: {student_info['Name']}")
            print(f"Email: {student_info['Email']}")
            print(f"Gender: {student_info['Gender']}")
            print("")

while True:
    print("\nStudent Management System Menu:")
    print("1. Add Record")
    print("2. Delete Record")
    print("3. Update Record")
    print("4. View Details")
    print("5. List All Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        delete_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        view_student()
    elif choice == "5":
        list_students()
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")