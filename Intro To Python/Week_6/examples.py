# File opening
with open("C.txt") as courses_file:
    for line in courses_file:
        print(line)

courses_file.close()

######################################################################
colors = "red green blue yellow"
# String splitting
color_parts = colors.split()
# ['red', 'green', 'blue', 'yellow']

print(colors)
print(color_parts)

for color in color_parts: # Good to use
    print(color)

second = color_parts[1] # prints the second second color in the color variable

print(second)

######################################################################
# Getting rid of whitespace from strings

name = "Brother Barnie      "

# clean_name = name.strip()   # Used to get rid of whitespace but doesn't change the elements of the variable
name = name.strip()           # Assigns the variable to itself so a new variable name isn't needed
print(f"---{name}---")
# print(f"---{clean_name}---")
######################################################################
# Reading files and parsing strings

with open("C.txt") as courses_file:
    for line in courses_file:
        # Line = "CSE 110,98.5"
        line.strip()
        parts = line.split(",")
        # Parts = ["CSE 110", "98.5"]
        name = parts[0]
        grade = float(parts[1])

        bonus_grade = grade + 3

        print(f"{name} - Grade: {grade}, after bonus: {bonus_grade}")
