shopping = []

user = ''
print("Please enter the items if the shopping list (type: quit to finish):")
while user != "quit":
    user = input("Item: ")
    if user != "quit":
        shopping.append(user)

print()            
print("Your shopping list is:")
for list in shopping:
    print(list)

print()
print("Your shopping list with indexes is:")
for i in range(len(shopping)):
    shop = shopping[i]
    print(f"{i}. {shop}")

print()
user = int(input("What item would you like to change? "))
new = input("What is the new item? ")

shopping[user] = new

print()
print("Your shopping list with indexes is: ")
for i in range(len(shopping)):
    shop = shopping[i]
    print(f"{i}. {shop}")