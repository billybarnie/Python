# Declared list with attached variable
friends = [] 

# This sets the names to empty
names = None

#This will keep asking the user to enter a name of a friend until they put in the word 'end'
while names != "end":
    names = input("Type the name of a friend: ")
    
    if names != "end":
        friends.append(names)

# This is an empty space         
print()
print("Your friends are:") # This lets them know that they have the name of friends list compiled

for friend in friends:
    print(friend) # This prints the names of said friends on their own line