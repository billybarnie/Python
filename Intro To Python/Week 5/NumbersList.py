tips = []

user_input = -1 

while user_input != 0:
    user_input = int(input("Enter a number: "))

    if user_input != 0:
        tips.append(user_input)

total = 0

for amount in tips:
    total += amount

print(f"The sum is: {total}")

add = len(tips)
grand = total / add

print(f"Your average is {grand}")
