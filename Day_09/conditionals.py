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
# Putting grades according the grades
# Get the score from user input
score = float(input("Enter your score (0-100): "))

# Validate score range and assign letter grade
if score < 0 or score > 100:
    print("Invalid score! Please enter a number between 0 and 100.")
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
if 0 <= score <= 100:
    print(f"Your score is {score}, which earns a Grade: {grade}")
# Getting the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is invalid, give feedback: "Invalid month. Please enter a valid month."
month = input("Enter a month: ").strip().capitalize()

autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]

if month in autumn:
    print(f"{month} is in Autumn.")
elif month in winter:
    print(f"{month} is in Winter.")
elif month in spring:
    print(f"{month} is in Spring.")
elif month in summer:
    print(f"{month} is in Summer.")
else:
    print("Invalid month entered! Please check your spelling.")

fruits = ["banana", "orange", "mango", "lemon"]

# Getting the fruit list
new_fruit = input("Enter a fruit name: ").strip().lower()

if new_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(new_fruit)
    print("Modified list:", fruits)
