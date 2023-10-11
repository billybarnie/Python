############################
# Author: Ian Barnie (Billy)
# Date: 1/29/23
# Teacher: Brown, Michael
# Class: CSE 110
############################

shopping_list = []          # This is an empty list built to hold item names 
balance = []                # Holds the amount of eah item in the shopping_list list

amount = -1                 # Sets the variable for amount from the user 
user_input = -1             # Sets the users input variable

while user_input != 5:      # This sets the program to run inside of a loop so long as the user doesn't input the number 5 in the options list
    print()
    print("Please select one of the following:")            # Prompts the user to input 1-5
    print("1. Add item")                                    # This speaks for itself as it allows them to add an item
    print("2. View cart")                                   # shows the contents of what was entered by the user to the shopping_list list and the cost (balance list)
    print("3. Remove item")                                 # This removes an item from the shopping list
    print("4. Compute total")                               # This gives the grad total of all the items in the shopping list
    print("5. Quit")                                        # Kills the program
    user_input = int(input("Please enter an action: "))     # asks the user to politely enter an action

    if user_input == 1: # Case 1
        print()
        user_input = input("What item would you like to add? ")             # Asks user for item name
        try:
            amount = float(input(f"What is the price of '{user_input}': ")) # Gets the price of say item from the user
        except ValueError:
            print("Invalid Response!")                                      # Outputs invalid response to the user
        else:
            balance.append(amount)                                          # Adds price to balance list
            shopping_list.append(user_input)                                # Adds item to shopping_list list
            print(f"'{user_input}' has been added to the cart.")            # Notifies the user that the item has been added to the card in hardcode
    elif user_input == 2: # Case 2
        print()
        print("The contents of the cart are: ")                         # Tells them the contents of the shopping_list list
        for i in range(len(shopping_list)):                             # Loops through the length of the shopping_list list one iteration at a time
            print(f"{i + 1}. {shopping_list[i]} - ${balance[i]:.2f}")   # This prints out the hardcode of each iteration from the for loop in <item> - <amount> formatting
    elif user_input == 3: # Case 3
        print()
        user_input = int(input("Which item would you like to remove (please enter the item NUMBER only)? "))    # Asks the user to remove item by index number NOT item name
        user_input = user_input - 1                                     # Minuses the users input from itself so the index removed matches the number the user wishes to remove
        shopping_list.pop(user_input)                                   # .pop() is used to then remove said index from shopping_list list
        balance.pop(user_input)                                         # .pop() is used to remove index cost from balance list
        print("Item removed")                                           # Notifies the user that said item has been removed
    elif user_input == 4: # case 4
        print()
        print(f"The total price of the items in the shopping cart is: ")    # Notifies the user of the total cost
        sum = 0                                                             # Sum variable declaration of zero
        for i in range(len(shopping_list)):                                 # Loops through each iteration of the length of shopping_list list
            sum += balance[i]                                               # Formula that is then used to combine each iteration together
        
        print(f"${sum:.2f}")                                                # Prints the sum variable of all loop iterations added together to the user informing them of cost due
        
        print()
        user_input = input("Would you like to pay here or in the store? (online/store): ")  # Prompts the user to pay in store or on here
        print()
        if user_input == "online":                                                          # If user types string "online" then it prompts the rest of the code inside the if statement
            print("Great! Your total has been paid in full.")                               # Notifies the user that they have paid in full
            shopping_list.clear()                                                           # This zeroes out the shopping_list list
            balance.clear()                                                                 # This zeroes out the cost of each item in balance list
            user_input = input("Would you like to continue shopping? (yes/no): ")           # Prompts the user with yes/no on whether they would like to continue shopping
            if user_input == "yes":                                                         # If user types string "yes" then it prompts the print statement in the if statement
                print("Awesome! Shop to your hearts content!")                              # Tells user to shop more essentially
            else:
                print("Thank you for shopping with us! Have a wonderful day!")              # If the user enters no on continue shopping it notifies the user to have a good day
                exit()                                                                      # Function is used to close the program once they have entered "no"
        if user_input == "store":                                                           # If the user inputs "store" then they can pay in the store if prefered
            print("Okay! I hope you enjoy the rest of your shopping experience!")           # Tells the user to enjoy the rest of their shopping

    else:
        if user_input == 5: # Case 5
            user_input = input("Are you sure you don't want to create another shopping list? (yes/no): ")   # Asks the user if they want to create another shopping list
            if user_input == "no":                                    # If user is't sure they don't want to create another list it will clear it lists and take them back to the menu
                shopping_list.clear()                                 # Clears shopping_list list
                balance.clear()                                       # Clears balance list for each item in shopping_list list
            else:
                print("Thank you. Goodbye!")                          # Tells the user goodbye
                exit()                                                # Function is used to exit the program
        else:
            if user_input > 5:                                        # This accounts for input validation so if the user inputs anther greater than 1-5 it gives the user an errer message
                print("Invalid response! Please enter options 1-5.")  # This Notifies the user that they have entered an invalid response