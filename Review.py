#Exercise 1: Check if a person is an adult or a minor
age=int(input("Enter Your Age : "))
if age>=18:
    print("Adult")
else:
    print("Minor")
#---------------------------------------
#Exercise 2: Print numbers from 1 to 5 using for
for i in range(1,6):
    print(i)
#----------------------------------------
#Exercise 3: Print even numbers from 1 to 10
for i in range(1,11):
    if i %2==0:
        print(i)
#---------------------------------------
# Exercise 4: Check if a number is positive, negative, or zero
number=int(input("Enter the number"))
if number>0:
    print("Positive")
elif number<0:
    print("Negative")
else:
    print("Zero")
#----------------------------------------
#Exercise5 :Print numbers from 1 to 5 using while
num=1
while num<=5:
    print(num)
    num=num+1
#----------------------------------------
#Exercise6 :1. Simple greet function
def greet():
    print("Hello Eklas")
