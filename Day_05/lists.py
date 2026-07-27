# Exercises - Day 05
# Declaring an empty list
empty_list = []
# Declaring a list with more than 5 items
web_techs = ["HTML", "CSS", "JavaScript", "React", "Python", "Redux"]
print(web_techs)
# Finding the length of the list that you just created
print("Length of the list: ", len(web_techs))
# Finding the first item, middle item and last item
print(
    "First, Middle and Last item: ",
    web_techs[0],
    web_techs[len(web_techs) // 2],
    web_techs[-1],
)
# New list with mix data types
mixed_data_types = ["Lourdes", 25, 5.01, "Married", "Miami Lakes, FL"]
print(mixed_data_types)
# New list with companies and values
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print("Length of the Companies list: ", len(it_companies))
print(
    "First, Middle and Last item: ",
    it_companies[0],
    it_companies[len(it_companies) // 2],
    it_companies[-1],
)
it_companies.pop()
print(it_companies)
it_companies.append("Intel")
print(it_companies)
it_companies.insert(len(it_companies) // 2, "Samsung")
print(it_companies)
it_companies[0] = it_companies[0].upper()
print(it_companies)
print("# ".join(it_companies))
print(it_companies.index("Samsung"))
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
first_three = it_companies[:3]
print(first_three)
last_three = it_companies[-3:]
print(last_three)
middle = len(it_companies) // 2
if len(it_companies) % 2 != 0:
    middle_companies = it_companies[middle : middle + 1]
else:
    middle_companies = it_companies[middle - 1 : middle + 1]
print(middle_companies)
it_companies.pop(0)
print(it_companies)
middle22 = len(it_companies) // 2
if len(it_companies) % 2 != 0:
    del it_companies[middle22]
else:
    del it_companies[middle22 - 1 : middle22 + 1]
print(it_companies)
it_companies.pop()
print(it_companies)
# Removing all the IT companies from the list
it_companies.clear()
print(it_companies)
# Destroy (Deleting) the IT companies list
del it_companies
# print(it_companies) #Showing error because there is none list with that name
# Creating two new lists
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
full_stack = front_end + back_end
print("Full Stack: ", full_stack)
# Creating a list of 10 students ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Finding the min and max age
# First I am sort the list and is going to be easier
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print("Minimum age: ", min_age)
print("Maximum age: ", max_age)
# Adding the new variables in the list (min_age, max_age)
ages.extend([min_age, max_age])
print(ages)
# Finding the median age
ages.sort()
n = len(ages)
med = n // 2
if n % 2 != 0:
    median_age = ages[med]
else:
    median_age = (ages[med - 1] + ages[med]) / 2
print("Median age: ", median_age)
average_age = sum(ages) // len(ages)
print("Average age: ", average_age)
range_age = max_age - min_age
print("Range age: ", range_age)
min_average = abs(min_age - average_age)
max_average = abs(max_age - average_age)
print("Minimum average: ", min_average)
print("Maximum average: ", max_average)
countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cabo Verde",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombia",
    "Comoros",
    "Congo, Democratic Republic of the",
    "Congo, Republic of the",
    "Costa Rica",
    "Côte d'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor (Timor-Leste)",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Eswatini",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Korea, North",
    "Korea, South",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "North Macedonia",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Palestine",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent and the Grenadines",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "South Sudan",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Sweden",
    "Switzerland",
    "Syria",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Togo",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe",
]
# Finding the middle contry or contries in the countries list
n = len(countries)
med = n // 2
if n % 2 != 0:
    countries_result = countries[med]
else:
    countries_result = (countries[med - 1] + countries[med]) / 2
print("Middle country or countries: ", countries_result)

# Diving the countries listo into two lists
mid_index = (len(countries) + 1) // 2
first_list = countries[:mid_index]
second_list = countries[mid_index:]
print("First List: ", first_list)
print("Second List: ", second_list)

# Unpacking some countries
new_countries = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
ch, ru, usa, *scandic_countries = new_countries
print("Unpacking the list of new countries: ")
print("ch: ", ch)
print("ru: ", ru)
print("usa: ", usa)
print("scandic countries: ", scandic_countries)
