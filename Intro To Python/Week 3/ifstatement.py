first_number = int(input("What is the first number? "))
second_number = int(input("What is the second number? "))
if first_number > second_number:
    print(f"First number is greater ")
else:
    print(f"first number is not greater ")
if first_number == second_number:
    print(f"The numbers are equal")
else:
    print(f"The numbers are not equal ")
if second_number > first_number:
    print(f"Second number is greater ")
else: 
    print(f"Second number is not greater ")
print()
favor_animal = "quail"
quail = str(input("What is your favorite animal? "))
if quail.lower() == favor_animal:
    print(f"Really? {quail} are my favorite animal too!")
else:
    print(f"{quail} aren't my favorite animal. ")