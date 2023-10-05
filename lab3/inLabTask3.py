class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []

    def add_marks(self, subject, score):
        self.marks.append((subject, score))

    def calculate_average(self):
        if not self.marks:
            return 0  # Return 0 if there are no marks
        total_score = sum(score for _, score in self.marks)
        return total_score / len(self.marks)

# Create an instance of the Student class
student1 = Student("M.Husnian", "101")

# Add marks for different subjects
student1.add_marks("Science", 79)
student1.add_marks("Math", 89)
student1.add_marks("History", 78)
student1.add_marks("English", 88)
student1.add_marks("Art", 90)

# Calculate and print the average marks
average_marks = student1.calculate_average()
print(f"Average Marks for {student1.name} with (Roll Number: {student1.roll_number}): {average_marks:.2f}")
