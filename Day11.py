# Functions - Day 11
# Declaring and calling a function
def generate_full_name():
    first_name = "Lourdes"
    last_name = "Pampa"
    space = " "
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())


# Function with parameters
def greetings(name):
    message = name + ", Welcome to Python!"
    return message


print(greetings("Lourdes"))


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


print("Age:", calculate_age(2026, 2001))


# Passing arguments with key and value
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


print(add_two_numbers(25, 29))


# Returning a boolean
def is_even(n):
    return n % 2 == 0


print(is_even(4))
print(is_even(6))
print(is_even(7))


# Returning a list
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens


print(find_even_numbers(10))
