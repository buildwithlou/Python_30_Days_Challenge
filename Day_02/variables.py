# Exercises - Level 1
firstName = "Lourdes"
lastName = "Pampa"
fullName = "Lourdes Pampa"
country = "Peru"
age, height, status = 25, 5.01, "Married"

# Exercises - Level 2
print(type(firstName))
print(type(lastName))
print(type(fullName))
print(type(country))
print(type(age))
print(type(height))
print(type(status))

print(50 * "-")
print(len(firstName))
print(len(lastName))
print(len(fullName))
print(len(country))
print(len(status))
# print(len(age)) #int has no length
# print(len(height)) #float has no length

# Compare the length of the first Name and last Name
print(50 * "-")
lenfirstName = len(firstName)
lenlastName = len(lastName)
print(f"{firstName} has {lenfirstName} letters")
print(f"{lastName} has {lenlastName} letters")

if lenfirstName > lenlastName:
    print(f"{firstName} is longer")
elif lenlastName > lenfirstName:
    print(f"{lastName} is longer")
else:
    print("They're the same length")

# Declaring num_one and num_two
print(50 * "-")
num_one = 5
num_two = 4
total = num_one + num_two
print(f"Total: {total}")
diff = num_one - num_two
print(f"Difference: {diff}")
product = num_two * num_one
print(f"Product: {product}")
division = num_one / num_two
print(f"Division: {division}")
remainder = num_one % num_two
print(f"Remainder: {remainder}")
exp = num_one**num_two
print(f"Exponent: {exp}")
floor_division = num_one // num_two
print(f"Floor Division: {floor_division}")
