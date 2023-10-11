print("This allows us to see if you can ride in this amusment park ride.")
print()


age = int(input("What is the age of the first rider? "))
height = float(input("What is the height of the first rider? "))
second_rider = input("Is there a second rider (Yes/ No)? ")

if age >= 15 and height >= 100:
    boo = True
    print("Welcome to the ride. Please be safe and have fun. ")
else:
    boo = False
    print("Sorry, you may not ride. ")

if second_rider.lower() == "yes" :
    boo = True
    age2 = int(input("What is the age of the second rider? "))
    hieght2 = float(input("What is the height of the second rider? "))
    if age2 >= 15 and height >= 100:
        boo = True
        print("Welcome to the ride. Please be safe and have fun.")
    else: 
        boo = False
        print("Sorry, you may not ride. ")
else:
    boo = False
