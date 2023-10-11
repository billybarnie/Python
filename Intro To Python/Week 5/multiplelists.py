checking = []
savings = []

users = ''

while users != "quit":
    users = input("What is the name of this account? ")
    
    if users != "quit":
        amount = float(input("What is the balance? "))
        savings.append(amount)
        checking.append(users)

whole = 0

print()
print("Account information:")
for i in range(len(checking)):
    print(f"{checking[i]} - ${savings[i]}")

    whole += savings[i]

entire = whole / len(savings)

print()
print(f"Total: ${whole:.2f}")
print(f"Average: ${entire:.2f}")






