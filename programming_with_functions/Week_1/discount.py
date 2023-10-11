from datetime import datetime

discount = .10
tax = .06

subtotal = float(input("Enter the subtotal here for possible discount: "))



current = datetime.now(tz=None)
weekday = current.weekday()

if subtotal >= 50 and (weekday == 1 or weekday == 2):
    dis = round(subtotal * discount, 2)
    print(f"Total discount is: ${dis:.2f}")
    subtotal -= dis
elif subtotal < 50 and (weekday == 1 or weekday == 2):
    whole = round(subtotal - 50, 2)
    print(f"You need ${whole:.2f} left to get a 10% discount.")

sale = round(subtotal * tax, 2)
print(f"Tax is: ${sale:.2f}")

total = subtotal + sale
print(f"Total: ${total:.2f}")
