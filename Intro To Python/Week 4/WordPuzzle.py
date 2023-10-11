print("Welcome to the word guessing game!")
print("You have 5 guesses. If none are correct the game will end, good luck!!")
print()

secret = "mosiah"
add = 1
guess = -1

print("Your hint is: _ _ _ _ _ _ ")
print()

while guess != secret:
    guess = input("What is your guess? ")
    guess = guess.lower()
    if len(guess) != len(secret):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        print()
        add += 1
        if add == 5:
            print("You failed! Better luck next time.")
            exit()
    elif guess == secret:
        print("Congratulations! You guessed it!")
        break
    elif add == 5:
        print("You failed! Better luck next time.")
        exit()
    else:
        add += 1
        print(f"Your hint is: ", end=" ")
        for index, letter in enumerate(guess):
            if letter == secret[index]:
                print(letter.upper(), end=" ")
            elif letter in secret:
                print(letter.lower(), end=" ")
            else:
                print("_", end=" ")
        if guess.lower() != secret.lower():
            print()
            print()
        else:
            print()
            print("Congratulations! You guessed it!")

print(f"It took you {add} guesses.")





