# Exercises - Day 09
# Getting user input using input("Enter your age: ")If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("Enter your age: "))
if age > 18 or age == 18:
    print("You are old enough to drive.")
else:
    print("You need ", 18 - age, " more years to learn to drive.")
# Comparing the vales of my_age and your_age using if ... else
my_age = 25
your_age = int(input("Enter your age: "))
if my_age > your_age:
    diff = my_age - your_age
    if diff == 1:
        print("I am 1 year older than you.")
    else:
        print("I am ", diff, " years older than you.")
elif my_age < your_age:
    diff = your_age - my_age
    if diff == 1:
        print("You are 1 year older than me.")
    else:
        print("You are ", diff, " years older than me.")
else:
    print("We are the same age.")
# Getting and comparing two numbers using if, elif, else
numberOne = int(input("Enter number one: "))
numberTwo = int(input("Enter number two: "))
if numberOne > numberTwo:
    print(numberOne, " is greater than ", numberTwo)
elif numberOne < numberTwo:
    print(numberOne, " is less than ", numberTwo)
else:
    print(numberOne, " is equal to ", numberTwo)
