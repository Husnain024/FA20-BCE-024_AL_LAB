
count = 1

while count <= 5:

    print(count)

count += 1

# 2. For Strings

# Using a while loop to print each character of a string text= "Hello"

text = "Hello"
index = 0

while index < len(text):

    print(text[index]) 
    index += 1

student_grades = {"Alice": 92, "Bob": 85, "Charlie": 78}

keys = list(student_grades.keys()) # Get the keys as a list

index = 0

while index < len (keys):

    key = keys[index]

value = student_grades[key] 
print (f" (key): {value}")

index += 1
