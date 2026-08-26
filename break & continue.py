
#Create a program that keeps asking the user for a password.
#If the password is "python123", print "Login successful" and stop the loop using break.
#Otherwise, print "Wrong password" and ask again.
while True:
    password=input("Enter your passwors : ")
    if password=="python123":
        print("Login Sccessful")
        break
else:
    print("Wrong password")


#Write a Python program that prints the numbers from 1 to 10, but skips the number 5.
for i in range(1,11):
    if i==5:
        continue
    print(i)




#Write a Python program that prints the numbers from 1 to 10.
#Stop the loop when the number reaches 6.
for i in range(1,11):
    if i==6:
        print("Number found!")
        break
    print(i)

#Write a Python program that prints the numbers from 1 to 20.
#Skip all even numbers using continue.
#The program should print only the odd numbers.
for i in range(1,21):
    if i % 2 == 0:
        continue
    print(i)

