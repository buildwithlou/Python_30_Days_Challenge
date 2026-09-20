# Tuples - Day 06
# Creating a tuple
empty_tuple = tuple()
# Creating a tuple with initial values
tpl = ("Item1", "Item2", "Item3")
fruits = ("banana", "orange", "mango", "lemon")
# length of the tuple
print(len(tpl))
# Accessing Tuple Items
first_item = tpl[0]
second_item = tpl[1]
# Slicing Tuples
all_item = tpl[0:4]  # all items
all_item = tpl[0:]  # all items
middle_two_items = tpl[1:3]
# Changing Tuples to Lists
lst = list(tpl)
# Checing item in a tuple
print("Item2" in tpl)  # True
# Joining Tuples
tpl2 = ("Item4", "Item5", "Item6")
tpl3 = tpl + tpl2
print(tpl3)
# Deleting Tuples
del tpl
