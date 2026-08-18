# Exercises - Day 10
# Iterate 0 to 10 using for loop
for i in range(11):
    print(i)
# Iterate 0 to 10 using while loop
count = 0
while count <= 10:
    print(count)
    count += 1
# Loop that makes a triangle
for i in range(1, 8):
    print("x" * i)
# Nested loop to make a figure
for row in range(8):
    for col in range(8):
        print("#", end=" ")
    print()
# Multiplication table using nested loop
for i in range(1, 11):
    print(f"{i} x {i} = {i * i}")
# Iterate through the list
frameworks = ["Numpy", "Pandas", "Django", "Flask"]
for framework in frameworks:
    print(framework)
# Using for loop to iterate from 0 to 100 and even numbers only
for i in range(101):
    if i % 2 == 0:
        print(i)
# Using for loop to iterate from 0 to 100 and odd numbers only
for i in range(101):
    if i % 2 != 0:
        print(i)
# Using for loop to iterate from 0 to 100 and print the sum of all numbers
sum = 0
for i in range(101):
    sum += i
print(f"The sum of all numbers is: {sum}")
# Using for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_evens = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i
print(f"The sum of all evens is {sum_evens}. And the sum of all odds is {sum_odds}.")
