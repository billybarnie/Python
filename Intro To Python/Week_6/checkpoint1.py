people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
age = 9999
person = ""

for persons in people:
    parts = persons.split()
    name = parts[0]
    number = int(parts[1])
    if number < age:
        age = number
        person = name

print(f"{person} is the youngest being {age} years old.")

