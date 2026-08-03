# Dictionaries - Day 08
# Creating an empty dictionary
empty_dict = {}
# Dictionary with data values
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
# Dictionary with real value
person = {
    "first_name": "Lourdes",
    "last_name": "Pampa",
    "age": "25",
    "country": "EEUU",
    "is_married": "True",
    "skills": ["Javascript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Miami Lakes", "zipcode": "33014"},
}
print(len(person))
# Accessing Dictionary Items
print(dct["key1"])
print(dct["key3"])
print(person["first_name"])
print(person["skills"][0])
print(person["address"]["street"])
# Checking if the value exists
print(person.get("first_name"))
print(person.get("country"))
print(person.get("skills"))
# Adding items to a dictionary
person["job_title"] = "DevOps Engineer"
person["skills"].append("HTML")
# Moving itmes in a dictionary
person["first_name"] = "Isabel"
person["last_name"] = "Suarez"
# Checking keys in a dictionary
print("country" in person)
# Removing items from a Dictionary
person.pop("age")  # removes age item
person.popitem()  # removes last item
# Changing dictionary to a list of items
print(person.items())  # items() changes dictionary to a list
print(dct.clear())  # clear() clear the whole information
del dct  # del deletes the dictionary
