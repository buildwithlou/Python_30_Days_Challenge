# Conditionals - Day 09
# If Condition; to know if the number is positive
a = 3
if a > 0:
    print("A is a positive number")
# If Else; to know if the number is positive or negative
a = -10
if a < 0:
    print("A is a negative number")
else:
    print("A is a positive number")
# If Elif Else; to know if the number is positive, negative or zero
a = 0
if a > 0:
    print("A is a positive number")
elif a < 0:
    print("A is a negative number")
else:
    print("A is zero")
# Nested Conditions; to know if the number is positive even integer, positive, zero or negative
a = 0
if a > 0:
    if a % 2 == 0:
        print("A is a positive and even integer")
    else:
        print("A is a positive number")
elif a == 0:
    print("A is zero")
else:
    print("A is a negative number")
# If condition and Logical Operators; to know if the number is positive even integer, positive, zero or negative
a = 0
if a > 0 and a % 2 == 0:
    print("A is an even and positive integer")
elif a > 0 and a % 2 != 0:
    print("A is a positive integer")
elif a == 0:
    print("A is zero")
else:
    print("A is a negative")
