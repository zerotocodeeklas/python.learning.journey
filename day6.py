# Exercise 1:
# Write a Python program that asks the user for their age.
# If the age is 18 or older AND less than 60,
# print "You are an adult".
# Otherwise, print "You are not an adult".
age=int(input("Enter your age: "))
if age>=18 and age<60:
    print("You are an adult")
else:
    print("You are not an adult")

# Exercise 2:
# Write a Python program that checks the day of the week.
# If the day is Friday OR Saturday, print "Weekend".
day="Friday"
if day=="Friday" or day=="Saturday":
    print("Weekend")


# Exercise 3:
# Create a variable called is_raining and set it to False.
# Use the not operator to check if it is not raining.
# If it is not raining, print "Go outside".
is_raining=False
if not is_raining:
    print("Go outside")

# Exercise 4:
# Write a Python program that asks the user for their age
# and whether they have an ID.
# The user can enter only if they are 18 or older
# AND they have an ID.
Age=int(input("Enter your age: "))
Has_ID=input("Do you have an ID ? ")

if age>=18 and Has_ID=="Yes":
    print("You Can Enter")
else:
    print("You Cannot Enter")