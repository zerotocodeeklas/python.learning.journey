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






