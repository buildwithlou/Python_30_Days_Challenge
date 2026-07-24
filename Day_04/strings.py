# Exercises - Day 04
# Concatenate strings
words = ["Thirty", "Days", "Of", "Python"]
sentence = " ".join(words)
print(sentence)
new_words = ["Coding", "For", "All"]
new_sentence = " ".join(new_words)
print(new_sentence)
company = " ".join(new_words)
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
