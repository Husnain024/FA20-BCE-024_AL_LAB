# Initialize a dictionary to store student names and grades
student_grades = {}

# Define the number of students
num_students = 7

# Input student names and grades
for _ in range(num_students):
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    student_grades[name] = grade

# Calculate and display the average grade
total_grade = sum(student_grades.values())
average_grade = total_grade / num_students
print(f"Average grade: {average_grade:.2f}")

# Categorize each student's grade and display
for student, grade in student_grades.items():
    if grade >= 90:
        category = "Excellent"
    elif grade >= 80:
        category = "Very Good"
    elif grade >= 70:
        category = "Good"
    else:
        category = "Needs Improvement"
    
    print(f"{student}: {grade} ({category})")

# Search for a specific student's grade
while True:
    search_name = input("Enter student name to search for (or 'quit' to exit): ")
    
    if search_name.lower() == 'quit':
        break
    
    if search_name in student_grades:
        print(f"{search_name}'s grade: {student_grades[search_name]}")
    else:
        print("Student not found. Please enter a valid name.")
