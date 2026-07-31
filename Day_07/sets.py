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
# Removing an item
it_companies.remove("Intel")
print(it_companies)
#  The difference between remove and discard in Python sets is that remove raises an error if
#  the item is not found in the set, while discard does not raise an error and simply does nothing
#  if the item is not present. Use remove when you want to ensure the item exists before removing it,
#  and discard when you don't care if the item is absent.
# Union of two sets
set_a = {"red", "blue", "yellow"}
set_b = {"purple", "green", "orange"}
sets_ab = set_a.union(set_b)
print("Union: ", sets_ab)
# Find intersections
intersect_ab = set_a.intersection(set_b)
print("Intersection: ", intersect_ab)
# Subset of the sets
subset_ab = set_a.issubset(set_b)
print("Subset: ", subset_ab)
