# Lists - Day 05
# Creating a list {both ways work}
# lst = list()
# empty_list = list()
# print(len(empty_list))

# lst = []
# empty_list = []
# print(len(empty_list))

# lst = ['Lourdes', '25', True, {'country': 'Peru', 'city': 'Lima'}]

lst = ["item1", "item2", "item3", "item4", "item5"]
first_item, second_item, third_item, *rest = lst
fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["tomato", "Potato", "Cabbage", "Onion", "Carrot"]
animal_products = ["milk", "meat", "butter", "yogurt"]
web_techs = ["HTML", "CSS", "JS", "React", "Redux", "NodeJS", "MongoDB"]
countries = ["Peru", "Cuba", "Japan", "Spain"]

# Adding an item in the list
fruits.append("apple")
fruits.append("lime")
# Adding in the specific index into the list
fruits.insert(2, "strawberries")
fruits.remove("banana")
# Deleting last item of the list
fruits.pop()
# Deleting the item that the index is specifying
del fruits[3]
# Reverse the list
fruits.reverse()

print("Fruits", fruits)
print("Number of fruits: ", len(fruits))
# Finding an item in the list
print(fruits.index("mango"))
print("Vegetables", vegetables)
print("Number of Vegetables: ", len(vegetables))
print("Animal Products: ", animal_products)
print("Number of Animal Products: ", len(animal_products))
print("Web Technologies: ", web_techs)
print("Number of Web Technologies: ", len(web_techs))
print("Countries: ", countries)
print("Number of Countries: ", len(countries))
print(first_item)
print(second_item)
print(third_item)
print(rest)
