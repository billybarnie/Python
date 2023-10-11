clients = []

#clients = ["Emily", "John", "Mary"] # This isn't really good to use, append useage is better.

# These add the names to the actual array
#clients.append("Emily")
#clients.append("John")
#clients.append("Mary")

#print(clients) #Not really useful to use as it prints out the brackets as well sadly
# Declare variable before the while so that it knows what you grab onto
new_client = " "
# It's generally good to go ahead and use a while loop on the input and that then adds input to the array as you can have it keep adding names to the array 
while new_client != "quit":
    new_client = input("What is the name of a client? ")
    clients.append(new_client)                              # This program will print out the word quit as the end but no worries all you need to is make an if statement

for client in clients:  # This is useful as it print the client names line by line
    print(client)       # you can add end=" " so that it print out the name on after the other on the same line with a space between them
    
#############################################################################################################################################################################

friends = ["Luc", "Kristi", "Rex"]  # Again not really useful
tips = [12.25, 13.95, 8.50]

# You must always declare the variable as stated previously
running_total = 0

for tip_amount in tips:
    #running_total = running_total + tip_amount # This goes through each iteration and adds each tip together and the below code block prints out the total tips added together
    running_total += tip_amount                 # This does the act same thing as the code block on lines 30


print(f"The total is: {running_total:.2f}")

#############################################################################################################################################################################

# Vocabulary

# This is an empty list to put items in later
moives = []

# To start the list with items in it you would simply do as follows
movies = ["Toy Story", "Pride and Prejudice", "Star Wars"]

# You can do the same thing with numbers that you can with strings
quiz_scores = [89.2, 78.5, 92.4, 93.8]

# It is best to avoid the use of the word list as a variable
list = []   # This is wrong do not do this 

