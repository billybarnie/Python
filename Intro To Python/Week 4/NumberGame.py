import random

again = "yes"

while again == "yes":
    number = random.randint(1, 100)
    count = 0
    guess = -1
    while guess != number:
        guess = int(input("What is your guess? "))
        count = count + 1

        if guess < number:
            print("Higher")
        elif guess > number:
            print("Lower")
        else:
            print("You guessed it!")

    print(f"It took you {count} guesses")

    again = input("Would you like to play again (yes/no)? ")

print()
print("Goodbye!")