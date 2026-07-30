# Exercises - Day 06
# Creating an empty tuple
tuple_example = tuple()
# Creating a tuple with my family names
Brothers = ("Max", "Ricardo", "Felipe", "Jhojan", "Luis")
Sisters = ("Nina", "Griselle", "Soledad")
Siblings = Brothers + Sisters
print("Siblings: ", Siblings)
# Length of Siblings
print("Lourdes have ", len(Siblings), " Siblings.")
# Adding names in my family tuple
Parents = ("Isabel", "Maximo")
Family = Siblings + Parents
print("Family: ", Family)
# Unpacking siblings and parents
*siblings, mother, father = Family
print("Siblings: ", siblings)
print("Parents: ", mother, father)
# Creating new tuples
fruits = ("mango", "strawberry", "banana", "pineapple")
vegetables = ("carrots", "avocados", "celery")
animal_products = ("treats", "leash")
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
print(type(food_stuff_lt))
middle = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 != 0:
    middle_food_stuff = food_stuff_lt[middle : middle + 1]
else:
    middle_food_stuff = food_stuff_lt[middle - 1 : middle + 1]
print(middle_food_stuff)
first_three_items = food_stuff_lt[0:3]
last_three_items = food_stuff_lt[-3:]
print(first_three_items)
print(last_three_items)
# Deleting the food_struff_tp completely
del food_stuff_tp
# checking if exists
# print(food_stuff_tp) #Giving us an error
