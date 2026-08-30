# Exercises - Day 11
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


print("Taking two parameters and returning the sum: ", add_two_numbers(5, 10))
print(50 * "#")


def circle_area(radius, pi=3.14):
    area = pi * radius**2
    return area


print("Calculating the area of a circle: ", circle_area(5))
print(50 * "#")


def called_all_nums(*args):
    for arg in args:
        if type(arg) not in (int, float):
            return f"Error: '{arg}' is not a valid number."
    return sum(args)


print("Calculating the sum of the next arguments: ", called_all_nums("r", 3, 5))
print(50 * "#")


def convert_celsius_to_fahrenheit(c):
    f = (c * 9 / 5) + 32
    return f


print("Converting temperature: ", convert_celsius_to_fahrenheit(3))
print(50 * "#")
