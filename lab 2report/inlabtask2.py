# Data Types - Dictionaries

phonebook = {}
phonebook["John"] = {"Phone": "012 794 794", "Email": "john@email.com"}
phonebook["Jill"] = {"Phone": "012 345 345", "Email": "jill@email.com"}
phonebook["Joss"] = {"Phone": "012 321 321", "Email": "joss@email.com"}
print(phonebook)

#Using for loop to extract data fron Dictionaries

for name, record in phonebook.items():
    print("{}'s phone number is {}, and email is {}" .format(name,record["Phone"], record["Email"]))
    