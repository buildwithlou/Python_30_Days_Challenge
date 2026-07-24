# Exercises - Day 04
# Concatenate strings
words = ["Thirty", "Days", "Of", "Python"]
new_words = ["Coding", "For", "All"]
sentence = " ".join(words)
new_sentence = " ".join(new_words)
company = " ".join(new_words)
big_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
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
