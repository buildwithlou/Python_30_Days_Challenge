# Exercises - Day 07
# sets
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Finding the length of the it_companies
print("The length of the it_companies set is: ", len(it_companies))
# Adding a value into the set
it_companies.add("Twitter")
print(it_companies)
# Adding multiple values into the set
it_companies.update(["Cisco", "Intel", "Dropbox"])
print(it_companies)
