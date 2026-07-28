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
