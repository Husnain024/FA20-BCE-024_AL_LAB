x = 2

y = 10

if x > 2:
    print("x > 2")

elif x == 2 and y > 50:
   print("x == 2 and y > 50")

elif x < 10 or y > 50:
    print("x < 10 or y > 50")
else:
    print("Nothing worked.")


name_list1 = ["John", "Jill"] 

name_list2 = ["John", "Jill"] 

print (not (name_list1 == name_list2))

# Using `is`

name2 = "John"

print(name_list1 == name_list2)

print(name_list1 is name_list2)
