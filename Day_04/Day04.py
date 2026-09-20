# Strings - Day 04

# Printing multiple lines, both ways work either ''' or """
multiline_string = """I am a student who wants to get better at Python
Because I want to get an internship as a DevOps Engineer, I know is going
to be hard but not imposible, I am getting use to write code everyday."""
print(multiline_string)

multiline_string_double = """I am doing my intership in a good company, they believed in me
and this is fun, I am having this internship from home and I am learning a lot of things,
I got a bunch of acknowledge by myself and it really helped me a lot."""
print(multiline_string_double)

# Printing a table with columns and rows
print(f"{'Days':<10} {'Topics':<10} {'Exercises':<10}")
print(f"{'Day 1':<10} {'5':<10} {'23':<10}")
print(f"{'Day 2':<10} {'6':<10} {'20':<10}")
print(f"{'Day 3':<10} {'5':<10} {'23':<10}")
print(f"{'Day 4':<10} {'1':<10} {'35':<10}")

# Formatted String
first_name = "Lourdes"
last_name = "Pampa"
language = "Python"
formated_string = "I am %s %s. I know %s" % (first_name, last_name, language)
print(formated_string)

python_libraries = ["Django", "Flask", "NumPy", "Matplotlib", "Pandas"]
formated_libraries = "The following are python libraries:%s" % (python_libraries)
print(formated_libraries)

husband_name = "William"
husband_lastname = "Suarez"
husband_formated = "My husband full name is {} {}.".format(
    husband_name, husband_lastname
)
print(husband_formated)

# Accessing Characters in Strings by Index
language = "Python"
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)
letter_last = language[-1]
print(letter_last)
letter_secondlast = language[-2]
print(letter_secondlast)
first_three = language[0:3]
print(first_three)
last_three = language[3:6]
print(last_three)
# Another way to print
three_last = language[-3:]
print(three_last)
three_lastlast = language[3:]
print(three_lastlast)
pto = language[0:6:2]
print(pto)

# String Methods
challenge = "thirty days of python"
challenge_Number = "30DaysPython"
sub_string = "da"
print(challenge.capitalize())
print(challenge.count("y"))
print(challenge.count("y", 7, 14))
print(challenge.count("th"))
print(challenge.endswith("on"))
print(challenge.endswith("tion"))
print(challenge.find("y"))
print(challenge.find("th"))
print(challenge.rfind("y"))
print(challenge.rfind("th"))
print(challenge.index(sub_string))
print(challenge.find(sub_string, 9))
print(challenge_Number.isalnum())
print(challenge_Number.isidentifier())
print(challenge.islower())
print(challenge.isupper())
print(challenge.strip("noth"))
print(challenge.replace("python", "coding"))
print(challenge.split())
print(challenge.split(", "))
print(challenge.title())
print(challenge.swapcase())
print(challenge.startswith("thirty"))

phrase = "thirsty\tdays\tof\tpython"
print(challenge.expandtabs())
print(challenge.expandtabs(20))

web_tech = ["HTML", "CSS", "JavaScript", "React"]
result = "".join(web_tech)
print(result)

web_technologies = ["HTML", "CSS", "JavaScript", "React"]
result = "# ".join(web_technologies)
print(result)
