# The point of this program is to ask the user for the cost of childrens meals and adults meals
# then add them together to get a subtotal and add the tax rate to the subtotal to get the final amount.

child = float(input("What is the price of a child's meal? "))          # Asks user for cost per child
adult = float(input("What is the price of an adult's meal? "))         # Asks user for cost per adult
beverages = float(input("What was that cost per drink? "))             # Asks user for cost per drink
children = int(input("How many children are there? "))                 # Asks user for amount of children
adults = int(input("How many adults are there? "))                     # Asks user for amount of adults
drink = int(input("How many drinks were ordered? "))                   # Asks user for the number of drinks obtained
rate = float(input("What is the sales tax rate? "))                    # Asks for tax rate
product = (children * child) + (adults * adult) + (drink * beverages)  # Formula for cost per child and adult combined
print()                                                                # Separater

number = '.2f'                                                         # Decimal formatter                 
print(f"Subtotal: ${product:,{number}}")                               # Prints formatted subtotal
tax = product * rate / 100                                             # tax rate formula 
print(f"Sales Tax: ${tax:,{number}}")                                  # Prints tax rate properly formatted
final = product + tax                                                  # formula adding tax rate solution to subtotal solution
print(f"Total for the food is: ${final:,{number}}")                    # Prints tax rate with subtotal which creates grand total
print()                                                                # Separater

bowling = float(input("What was the cost the bowling ticket? "))       # User is asked for amount of bowling tickets
person = float(input("How many tickets were purchased? "))             # User is asked for the number of tickets purchased
shoes = float(input("What were the number of shoes needed? "))         # User is asked for the number of shoes needed
whole = float(input("What was the cost per pair of shoes? "))          # User is asked for the amount that each pair of shoes cost
grand = (bowling * person) + (whole * shoes) + final                   # The formaula is used to add to the final
print(f"Total with the bowling alley and food is: {grand:.2f}")        # This prints the total for the bowling alley
print()

# In the below area where the user is asked for a coupon takes the total and subtracts the discount from the grand total 
# before it is then paid for by the user. This is something that I decided to add in place as a form of creativity to lower
# any high cost the user might be facing if they are on a budget. 
discount = float(input("Did you have a coupon and if so what was the amount on said coupon? "))
entire = grand - discount
print(f"Your new total with the coupon applied is: ${entire:.2f}")     # This outputs the new total with the coupon applied
amount = float(input("What is the payment amount? "))                  # The amount the user is paying with
print()
change = amount - entire                                               # formula taking grand total out of amount paid with
print(f"Change: ${change:,{number}} is due")                           # Prints what is left of the amount


# In the code above when asked for the cost of bowling I implemented this inside of my code as a form of creativity to see if they
# went bowling in the same building that they ate at or not. If the cost of the bowling and asking for shoes were all zero then 
# it can be assumed that they didn't go bowling. I also asked them if they had gotten any drinks as drinks were not refillable as the
# place the user had gone to. I am going to assume they went to main event though which is a popular place in texas to go for gaming, 
# food, as well as bowling. No taxes are added for the cost of the bowling. 