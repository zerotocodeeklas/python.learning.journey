#Create a dictionary called student.Add the following information:name,age,major,Then print the dictionary.
Student={
    "name":"Noor",
    "age":23,
    "major": "Computer Science"
}
print(Student)

#Create a dictionary containing your name, age, and city.Print your name separately using its key.Print your age separately using its key.

My_Information={
    "Name":"Eklas",
    "Age":24,
    "city":"Muscat"
}
print(My_Information["name"])
print(My_Information["Age"])

#Create a dictionary called student containing a student's name and age.Change the student's age.Then print the dictionary.
Student = {
    "Name": "Kawther",
    "age": "25"
}
Student["age"] = 23
print(Student)

#Create a dictionary containing:name = Eklas,age = 24,major = Computer Science.Then:Delete major&Print the dictionary.
personal_info={
    "name":"Eklas",
    "age":24,
    "major":"CS"
}
personal_info.pop("major")
print(personal_info)

#Create a dictionary containing:name = Eklas,age = 24,city = Muscat,major = Computer Science.Then:Print the dictionary,Print the number of items in the dictionary using len().
personal_info={
    "name":"Eklas",
    "Age":24,
    "City":"Muscat",
    "major":"CS"
}
print(personal_info)
print(len(personal_info))

#Create a dictionary containing name, age, and city. Use a for loop to print each key and its value.
info={
    "name":"Eklas",
    "age":24,
    "city":"Muscat"
}
for key in info:
    print(key,":",info[key])

#Search in a Dictionary:Create this dictionary.Ask the user to enter a key. If the key exists, print its value.If the key does not exist, print:Key not found
Dictionary_info={
    "name":"Eklas",
    "age":24,
    "major":"CS"
}
key = input("Enter a key: ")
if key in Dictionary_info:
    print(Dictionary_info[key])
else:
    print("Key not found")

---------
Q1={
    "name":"Eklas",
    "age":24,
    "major":"CS"    
}
print(Q1["name"])

--------------
Q2 = {
    "name": "Eklas",
    "age": 24,
    "city": "Muscat"
}
Q2["age"] = 25
print(Q2)

---------
Q3 = {
    "name": "Eklas",
    "age": 24,
    "major": "CS"
}
Q3["city"] = "Muscat"
Q3.pop("major")
print(Q3)

-----------
Q4={
    "name":"Eklas",
    "age":24,
    "major": "CS"
}
for key in Q4:
    print(key,":",Q4[key])

-----------
Q5={
    "name":"Eklas",
    "age":24,
    "major":"CS"
}
key = input("Enter a key: ")
if key in Q5:
    print(Q5[key])
else:
    print("Key not found")

----------
student = {
    "name": "Eklas",
    "age": 24,
    "major": "CS"
}
student["age"] = 25
student["city"] = "Muscat"
student.pop("major")
for key in student:
    print(key, ":", student[key])
