#Ask the user to enter their username.
#If the username is "Eklas", print "Welcome Eklas!".
#Otherwise, print "Unknown user".
Username=input("Enter the user name :")
if Username=="Eklas":
    print("Welcome Eklas")
else:
    print("Unknown User")



#Ask the user to enter their age.
#If the age is 18 or older, print "Adult".
#Otherwise, print "Minor".
Age=int(input("Enter your age: "))
if Age>=18:
    print("Adult")
else:
    print("Minor")



#Ask the user to enter the price of a product.
#If the price is greater than or equal to 100, print "Expensive".
#Otherwise, print "Affordable".
Price=float(input("Enter the price of a product :"))
if Price>=100:
    print("Expensive")
else:
    print("Affordable")


#Ask the user for their username and age.
#If the username is "Eklas" AND the age is 18 or older, print:
#"Access granted"
#Otherwise, print:
#"Access denied"
username=input("Enter the username: ")
age=int(input("Enter Your age :"))
if username=="Eklas" and age>=18:
    print("Access granted")
else:
    print("Access denied")