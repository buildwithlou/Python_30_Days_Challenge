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


def check_season(month):
    month = month.capitalize()
    if month in ("September", "October", "November"):
        return "Autumn"
    if month in ("December", "January", "February"):
        return "Winter"
    if month in ("March", "April", "May"):
        return "Spring"
    if month in ("June", "July", "August"):
        return "Summer"
    else:
        return "Invalid month name"


print("Season depending of the month: ", check_season("june"))
print(50 * "#")


def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return "Slope is undefined (vertical line)"
    slope = (y2 - y1) / (x2 - x1)
    return slope


print("Returning the slope: ", calculate_slope(1, 2, 3, 6))
print(50 * "#")


def solve_quadratic_eqn(a, b, c):
    # Quadratic Formula: ax^2 + bx + c = 0
    if a == 0:
        return "a cannot be 0"
    # Finding the discriminant: b^2 - 4ac
    d = b**2 - 4 * a * c
    if d >= 0:
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d**0.5) / (2 * a)
        return (x1,) if x1 == x2 else (x1, x2)
    else:
        real = -b / (2 * a)
        imag = (-d) ** 0.5 / (2 * a)
        return (complex(real, imag), complex(real, -imag))


print("Solving a quadratic equation: ", solve_quadratic_eqn(1, -3, 2))
print(50 * "#")


def print_list(lst):
    for item in lst:
        print(item)


wishlist = [
    "dyson airwarp",
    "pink brushes",
    "a dachshund puppy",
    "a new entretainment center",
    "kindle",
]
print_list(wishlist)
print(50 * "#")


def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        # range(start, stop, step)
        reversed_arr.append(arr[i])
    return reversed_arr


print("Printing reverse of the array: ", reverse_list([1, 2, 3, 4, 5]))
print("Printing reverse of the array:: ", reverse_list(["A", "B", "C"]))
print(50 * "#")


def capitalize_list_items(lst):
    capitalize_lst = []
    for item in lst:
        capitalize_lst.append(item.capitalize())
    return capitalize_lst


print(
    "Printing capitalize list items: ",
    capitalize_list_items(
        ["miu miu", "prada", "Dior", "Loewe", "Lululemon", "Loro Piana"]
    ),
)
print(50 * "#")


def add_item(lst, param):
    lst.append(param)
    return lst


food_stuff = ["Potato", "Tomato", "Mango", "Milk"]
print("New list adding the parameter: ", add_item(food_stuff, "Meat"))
print(50 * "#")


def remove_item(lst, param):
    lst.remove(param)
    return lst


food_stuff = ["Potato", "Tomato", "Mango", "Milk"]
print(remove_item(food_stuff, "Mango"))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
print(50 * "#")


def sum_of_numbers(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total


print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100))  # 5050
print(50 * "#")


def sum_of_odds(num):
    total = 0
    for i in range(1, num + 1, 2):
        total += i
    return total


print("Printing the sum of odds: ", sum_of_odds(5))
print(50 * "#")


def sum_of_even(num):
    total = 0
    for i in range(2, num + 1, 2):
        total += i
    return total


print("Printing the sum of evens: ", sum_of_even(5))
print(50 * "#")


def evens_and_odds(param):
    evens = 0
    odds = 0
    for i in range(param + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1

    print(f"The number of odds are {evens}")
    print(f"The number of evens are {odds}")


evens_and_odds(100)
print(50 * "#")


def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)


print("Printing the factorial ", factorial(5))
print(50 * "#")


def is_empty(param):
    return bool(not param)


print("The param is:", is_empty(""))


def calculate_mean(lst):
    return sum(lst) / len(lst)


def calculate_median(lst):
    nums = sorted(lst)
    n = len(nums)

    if n % 2 == 1:
        return nums[n // 2]
    else:
        middle1 = nums[n // 2 - 1]
        middle2 = nums[n // 2]
        return (middle1 + middle2) / 2


print("Calculating mean", calculate_mean([10, 20, 30, 40, 50]))
print("Calculating mean", calculate_median([20, 10, 30, 40, 50, 60]))
