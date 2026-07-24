# Exercises - Day 04
# Concatenate strings
words = ["Thirty", "Days", "Of", "Python"]
new_words = ["Coding", "For", "All"]
sentence = " ".join(words)
new_sentence = " ".join(new_words)
company = " ".join(new_words)
big_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
PFE = "Python For Everyone"
CFA = "Coding For All"
CFAwS = " Coding For All      "
CFAP = "Coding For All People"
conjunction = "You cannot end a sentence with because because because is a conjunction"
python_libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
radius = 10
area = 3.14 * radius**2
a = 8
b = 6
print(sentence)
print(new_sentence)
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:])
print(company.find("Coding"))
print(company.replace("Coding", "Python"))
print(company.replace("Coding For All", "Python For Everyone"))
print(company.split(" "))
print(big_companies.split(", "))
print(company[0])
print(company[-1])
print(company[10])
print(CFA.index("C"))
print(CFA.index("F"))
print(CFAP.rfind("l"))
print(conjunction.index("because"))
print(conjunction.rindex("because"))
print(conjunction[31:54])
print(conjunction.find("because"))
print(CFA.startswith("Coding"))
print(CFA.endswith("Coding"))
print(CFAwS.strip())
print("thirty_days_of_python".isidentifier())
print("# ".join(python_libraries))
print("I am enjoying this challenge. \nI just wonder what is next.")
print(f"{'Name':<10} {'Age':<10} {'Country':<10} {'City':<10}")
print(f"{'Lourdes':<10} {'25':<10} {'EEUU':<10} {'Miami':<10}")
print(f"The area of a circle with radius {radius} is {area} meters square ")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a**b}")
