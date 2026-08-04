# Creating an empty dictionary called dog
dog = {}
# Adding items to the dictionary
dog["name"] = "Francisco"
dog["color"] = "Chocolate dapple"
dog["breed"] = "Dachshund"
dog["legs"] = 4
dog["age"] = "4 weeks"
print(dog)
# Creting another dictionary called student
student = {
    "first_name": "William",
    "last_name": "Suarez",
    "gender": "Men",
    "age": "29",
    "marital status": "Married",
    "skills": ["Bookepping", "Accountant", "Finance"],
    "country": "USA",
    "city": "Miami Lakes",
    "address": "15525 Miami Lakeway N",
}
# Getting the length of the last dictionary
print("Length of Student Dictionary: ", len(student))
# Getting the value of skills and check the data type
print("Skills: ", student["skills"])
print("Skills Data Type: ", type(student["skills"]))
# Modifying the skills value by adding one or two skills
student["skills"].append("Budgeting")
student["skills"].append("Taxation")
student["skills"].append("Attention to Detail")
print("Skills: ", student["skills"])
# Getting the dictionary keys as a list
keys_list = list(student.keys())
print("Keys List: ", keys_list)
# Getting the dictionary values as a list
values_list = list(student.values())
print("Keys Values: ", values_list)
# Changing the dictionary to a list of tuples
print("Changing the dictionary to a list of tuples: ", list(student.items()))
# Deleting one if the items in the dictionary
student.pop("age")
print("Student: ", student)
