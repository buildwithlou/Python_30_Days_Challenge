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
# For loop; we use to make a for loop iterating over a sequence
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)
language = "Python"
for letter in language:
    print(letter)
for i in range(len(language)):
    print(language[i])
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)  # this way we get both keys and values printed out
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
for company in it_companies:
    print(company)

# Break and continue; we use it when we want to stop our loop before it is completed
numbers = (0, 1, 2, 3, 4, 5)
