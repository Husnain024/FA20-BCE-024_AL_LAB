
# Data Types - Dictionaries

phonebook = {}
phonebook["John"] = {"Phone": "012 794 794", "Email": "john@email.com"}
phonebook["Jill"] = {"Phone": "012 345 345", "Email": "jill@email.com"}
phonebook["Joss"] = {"Phone": "012 321 321", "Email": "joss@email.com"}
print(phonebook)

#Using for loop to extract data fron Dictionaries

for name, record in phonebook.items():
    print("{}'s phone number is {}, and email is {}" .format(name,record["Phone"], record["Email"]))
    
# First `del`

del phonebook["John"]
for name, record in phonebook.items():
    print("{}'s phone number is {}. \ and their email is {}" .format(name, record["Phone"], record["Email"]))

# Pop returna the record and deletes it 

jill_record = phonebook.pop("Jill")
print(jill_record)
for name, record in phonebook.items():
    #you can see that only joss is still left in the system
    print("{}'s phone number is {}. \ and their email is {}" .format(name, record["Phone"], record["Email"]))

#del phonebook["John"]
