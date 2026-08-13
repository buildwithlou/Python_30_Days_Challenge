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
