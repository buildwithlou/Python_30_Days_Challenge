# Loops - Day 10
# While loop; we use it to execute a block of statements repeatedl until a given condition is satisfied
count = 0
while count < 5:
    print(count)
    count += 1
# Break and continue; we use break when we like to get out for or stop the loop, and we continue statement we can can skip the iteration
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1
