#Create an empty list called names.Ask the user to enter their name and add the name to the list using append().Finally, print the list.
names=[]
name=input("Enter Your name :")
names.append(name)
print(names)



#Create an empty list called numbers.Ask the user to enter five numbers using a for loop.Add each number to the list.Finally, print the list.
numbers = []
for i in range(5):
    number = int(input("Enter the number:"))
    numbers.append(number)
print(numbers)


#Create an empty list called names.Ask the user to enter three names using a for loop.Add each name to the list.Finally, print the list.
Names=[]
for i in range(3):
    Name=input("Enter the Name :")
    Names.append(Name)
print(Names)


#Create a list of five numbers.Use sum() to calculate and print the total of the numbers.
Numbers=[]
for i in range(5):
    Number=int(input("Enter the number :"))
    Numbers.append(Number)
print("Total ",sum(Numbers))



#Ask the user to enter five numbers.Store the numbers in a list.Then print:
#The list
#The total number of elements
#The sum of the numbers

Num = []
for i in range(5):
    num = int(input("Enter the number: "))
    Num.append(num)
print("Numbers:", Num)
print("Number of elements:", len(Num))
print("Total:", sum(Num))
