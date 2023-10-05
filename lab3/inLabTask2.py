def calculate_gpa(students):
    # Dictionary to map percentage ranges to grade points
    grade_point_mapping = {
        (85, 100): 4.00,
        (80, 84): 3.66,
        (75, 79): 3.33,
        (71, 74): 3.00,
        (68, 70): 2.66,
        (64, 67): 2.33,
        (61, 63): 2.00,
        (58, 60): 1.66,
        (54, 57): 1.30,
        (50, 53): 1.00,
        (0, 49): 0.00,
    }

    result = []
    
    for student in students:
        name = student['name']
        marks = student['marks']
        
        # Calculate the grade point for each course
        grade_points = []
        for mark in marks:
            percentage = (mark / 100) * 100
            
            # Determine the grade point based on the percentage
            grade_point = None
            for (min_range, max_range), gp in grade_point_mapping.items():
                if min_range <= percentage <= max_range:
                    grade_point = gp
                    break
            
            grade_points.append(grade_point)
        
        # Calculate GPA by averaging the grade points
        gpa = sum(grade_points) / len(grade_points)
        
        # Create the student's record
        student_record = {
            'name': name,
            'grades': marks,
            'grade_points': grade_points,
            'gpa': gpa
        }
        
        result.append(student_record)
    
    return result

# Example student records
students = [
    {'name': 'Ali', 'marks': [75, 88, 75, 83, 82]},
    {'name': 'Babar', 'marks': [67, 77, 75, 69, 65]},
    {'name': 'Uzair', 'marks': [81, 68, 78, 82, 84]},
    {'name': 'Eman', 'marks': [91, 86, 69, 72, 61]},
    {'name': 'Sidra', 'marks': [88, 56, 71, 50, 51]}
]

# Calculate GPA for the students
gpa_results = calculate_gpa(students)

# Print the results
for student in gpa_results:
    print(f"Name: {student['name']}")
    print(f"Grades: {student['grades']}")
    print(f"Grade Points: {student['grade_points']}")
    print(f"GPA: {student['gpa']}")
    print()
