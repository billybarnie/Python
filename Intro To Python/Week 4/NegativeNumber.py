positive = int(input("Please enter a positive number: "))

while positive < 0:
    print("Sorry, that is a negative number. Please try again.")
    positive = int(input("Please enter a positive number: "))

if positive > 0:
    print(f"The number is: {positive}")