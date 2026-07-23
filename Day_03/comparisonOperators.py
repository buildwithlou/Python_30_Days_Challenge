import math

# Variables
age = 25
height = 5.01
Cnumber = 1 + 3

# User entering the base and height of the triangle and calculate the area of this triangle
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

# User enter side a, b and c of the triangle and calculate the perimeter of the triangle
print("#" * 50)
sideA = int(input("Enter side a: "))
sideB = int(input("Enter side b: "))
sideC = int(input("Enter side c: "))
perimeterTriangle = sideA + sideB + sideC
print(f"The perimeter of the triangle is {perimeterTriangle}")

# Getting length and width of a rectangle to calculate the area and perimeter
print("#" * 50)
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")

# Getting radius of a circle to calculate the area and circumference
print("#" * 50)
pi = 3.14
radius = int(input("Enter the radius: "))
areaCircle = pi * radius * radius
circumference = 2 * pi * radius
print(f"The area of the circle is: {areaCircle}")
print(f"The circumference of the circle is: {circumference}")

# Calculating the slope
m = 2
b = -2
x_intercept = -b / m
y_intercept = b
print(f"Slope (m): {m}")
print(f"Y-intercept: (0, {y_intercept})")
print(f"X-intercept: (0, {x_intercept})")

# Calculating the slope ( m = y2 - y1 / x2 - x1) and the Euclidean distance
x1, x2 = 2, 2
y1, y2 = 6, 10

if x2 == x1:
    mm = None
    print("The line is vertical, so the slope is undefined")
elif y1 == y2:
    mm = None
    print("The line is vertical, so the slope is undefined")
else:
    mm = (y2 - y1) / (x2 - x1)
    print(f"The slope for point(2,2) and point(6,10) is {mm}")
d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(f"The Euclidean distance between point(2,2) and point (6,10) is {d}")

# Comparing the slopes in tasks 8 and 9
if m is None and mm is None:
    print("Both slopes are undefined (both are vertical lines).")
elif m is None:
    print("The first slope (m) is undefined, so it cannot be compared numerically.")
elif mm is None:
    print("The second slope (mm) is undefined, so it cannot be compared numerically.")
elif m > mm:
    print(f"{m} is the biggest number")
elif mm > m:
    print(f"{mm} is the biggest number")
else:
    print("They've the same value")

# Calculate the value of y
# Formula => y = x^2 + 6x +9
for x in range(-10, 11):
    # Calculating y using the equation
    y = (x**2) + (6 * x) + 9
    print(f"When x = {x:3d}, y = {y}")
    # Checking if y is 0
    if y == 0:
        print(f"y is 0 when x = {x}")

# Finding the length of 'Python' and 'Dragon'
p = "Python"
d = "Dragon"
print("Length of Python: ", len(p))
print("Length of Dragon: ", len(d))
Different = len(p) != len(d)
print(Different)
