# Exercises - Day 05
# Declaring an empty list
empty_list = []
# Declaring a list with more than 5 items
web_techs = ["HTML", "CSS", "JavaScript", "React", "Python", "Redux"]
print(web_techs)
# Finding the length of the list that you just created
print("Length of the list: ", len(web_techs))
# Finding the first item, middle item and last item
print(
    "First, Middle and Last item: ",
    web_techs[0],
    web_techs[len(web_techs) // 2],
    web_techs[-1],
)
# New list with mix data types
mixed_data_types = ["Lourdes", 25, 5.01, "Married", "Miami Lakes, FL"]
print(mixed_data_types)
# New list with companies and values
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print("Length of the Companies list: ", len(it_companies))
print(
    "First, Middle and Last item: ",
    it_companies[0],
    it_companies[len(it_companies) // 2],
    it_companies[-1],
)
it_companies.pop()
print(it_companies)
it_companies.append("Intel")
print(it_companies)
it_companies.insert(len(it_companies) // 2, "Samsung")
print(it_companies)
it_companies[0] = it_companies[0].upper()
print(it_companies)
print("# ".join(it_companies))
print(it_companies.index("Samsung"))
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
first_three = it_companies[:3]
print(first_three)
last_three = it_companies[-3:]
print(last_three)
middle = len(it_companies) // 2
if len(it_companies) % 2 != 0:
    middle_companies = it_companies[middle : middle + 1]
else:
    middle_companies = it_companies[middle - 1 : middle + 1]
print(middle_companies)
it_companies.pop(0)
print(it_companies)
middle22 = len(it_companies) // 2
if len(it_companies) % 2 != 0:
    del it_companies[middle22]
else:
    del it_companies[middle22 - 1 : middle22 + 1]
print(it_companies)
it_companies.pop()
print(it_companies)
# Removing all the IT companies from the list
it_companies.clear()
print(it_companies)
# Destroy (Deleting) the IT companies list
del it_companies
# print(it_companies) #Showing error because there is none list with that name
# Creating two new lists
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
full_stack = front_end + back_end
print("Full Stack: ", full_stack)
