#Write a Python program that uses a while loop to print the numbers from 1 to 5.
number=1
while number <=5:
    print(number)
    number=number+1

#Write a Python program that uses a while loop to print the numbers from 5 down to 1.
num=5
while num >0:
    print (num)
    num=num-1


#Write a Python program that keeps asking the user to enter a password while the password is incorrect.
#The correct password is "python123".
#When the user enters the correct password, print "Login successful".
password=""
while password !="python123":
    password=input("Enter the password : ")
print("Login successful")


#Ask the user to enter a number.
#Use a while loop to print the numbers from 1 up to that number.

num = int(input("Enter the number: "))
count = 1
while count <= num:
    print(count)
    count = count + 1