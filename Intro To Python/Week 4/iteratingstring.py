com = "Commitment"

letters = input("What is your favorite letter? ")

for let in letters:
    if let.lower() == letters.lower():
        print(let.upper(), end="")
    else:
        print(let.lower(), end="")
print()

for let in letters:
    if let.lower() == letters.lower():
        print("_", end="")
    else:
        print(let.lower(), end="")