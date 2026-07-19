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
