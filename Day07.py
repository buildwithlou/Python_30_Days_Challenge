# Sets - Day 07
# Creating an empty set
st = set()
# Creating a set with initial items
st = {"item1", "item2", "item3", "item4"}
# Finding the length of a set
print(len(st))
# Checking if an item exists in a set
print("item2" in st)
# Adding one item
st.add("item5")
print(st)
# Adding multiple items
st.update(["item6", "item7", "item8"])
print(st)
# Removing items from a set
st.remove("item2")
print(st)
# Removin a random item in a set
st.pop()
print(st)
# Deleting a set
# del st
# Converting a list to a set
# syntax
lst = ["item1", "item2", "item3", "item4", "item1"]
st = set(lst)
# Joining sets
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item5", "item6", "item7", "item8"}
st3 = st1.union(st2)
# Finding interseciton Items
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item3", "item2"}
st1.intersection(st2)
# Checking subset and super set
# syntax
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item2", "item3"}
print(st2.issubset(st1))
print(st1.issuperset(st2))
# Checking difference between two sets
# syntax
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item2", "item3"}
print(st2.difference(st1))
print(st1.difference(st2))
