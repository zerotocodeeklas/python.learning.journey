#Create a list called fruits containing three fruits. Print the list.
Fruits=["Apple","Banana","Orange"]
print(Fruits)

#Create a list containing three names.Print the first name, the second name, and the third name separately.
Names=["Eklas","Noor","Kawther"]
print(Names[0])
print(Names[1])
print(Names[2])

#Create a list containing three cities.Change the second city to "Muscat".Then print the list.

Cities=["Salalah", "Sohar","Bahla"]
Cities[1]="Muscat"
print(Cities)

#Create a list containing three programming languages.Add "Java" to the list using append().Then remove one programming language using remove().Finally, print the list.
Languages=["C++","Python","JavaScript"]
Languages.append("Java")
Languages.remove("C++")
print(Languages)

#Create a list containing five programming languages.Use a for loop to print each programming language separately.
programming_languages=["Python","Java","C++","JavaScript","PHP"]
for programming in programming_languages:
    print(programming)


#Create a list containing five numbers.Use a for loop to print each number.Then use len() to print the total number of elements in the list.
Numbers=[10,20,30,40,50]
for number in Numbers:
    print(number)
    print(len(Numbers))



