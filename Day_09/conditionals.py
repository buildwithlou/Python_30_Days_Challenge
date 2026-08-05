# Exercises - Day 09
# Getting user input using input("Enter your age: ")If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("Enter your age: "))
if age > 18 or age == 18:
    print("You are old enough to drive.")
else:
    print("You need ", 18 - age, " more years to learn to drive.")
