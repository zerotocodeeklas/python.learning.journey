# Exercise:
# Write a program that asks the user for their grade
# and displays the appropriate result.

grade=int(input("Enter your Grade : "))
if grade>=90:
    print("Excellent")
elif grade>=80:
    print("Very Good")
elif grade>=70:
    print("Good")
elif grade>=50:
    print("pass")
else:
    print("Fail")


#Ask the user for a number and determine whether it is positive, negative, or zero.
Number=int(input("Enter a number :"))
if Number>0:
    print("Positive")
elif Number<0:
    print("Negative")
else:
    print("Zero")

#Ask the user for their age and determine whether they are a child, teenager, adult, or senior.
Age=int(input("Enter your age : "))
if Age<13:
    print("child")
elif Age<18:
    print("Teenager")
elif Age<60:
    print("Adult")
else:
    print("Senior")


#Ask the user for a password. If it is correct, display "Correct password". If the password is "python", display "Password is too short". Otherwise, display "Wrong password".
password=input("Enter the password : ")
if password=="python123":
    print("Correct password")
elif password=="python":
    print ("Password is too short")
else:
    print("Wrong password")
