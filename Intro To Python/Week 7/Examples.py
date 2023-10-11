from datetime import datetime
# Prints the current time
def print_time():               # def creates a function the programmer desires
    print("Tasks completed")    
    print(datetime.now())  # prints the date time
    print()

first_name = "Susan"
print_time()

for x in range(0, 10):
    print(x)
print_time()    # calls definition
#####################################################
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = "Susan"
print_time("first name assigned")

for x in range(0,10):
    print(x)
print_time("loop completed")
#####################################################
# Without function
first_name = input("Enter your first name: ")
first_name_initial = first_name[0:1]
last_name = input("Enter your last name: ")
last_name_initial = last_name[0:1]

print("Your initials are: " + first_name_initial \
    + last_name_initial)
#####################################################
# With function
def get_initial(name):
    initial = name[0:1]
    return initial

first_name = input("Enter your first name: ")
first_name_initial = get_initial(first_name)

last_name = input("Enter your last name: ")
last_name_initial = get_initial(last_name)

print("Your initials are: " + first_name_initial \
    + last_name_initial)

#####################################################

def get_initial(name, force_uppercase):
    initial = name[0:1]
    return initial
first_name = input("Enter your first name: ")
first_name_initial = get_initial(first_name, False)

middle_name = input("Enter your middle name: ")
middle_name_initial = get_initial(middle_name, False)

last_name = input("Enter your last name: ")
last_name_initial = get_initial(last_name, False)

print("Your initials are: " + first_name_initial \
    + middle_name_initial + last_name_initial)
#####################################################

def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return

first_name = input("Enter your first name: ")
first_name_initial = get_initial(force_uppercase=True,\
                                    name=first_name)

print("Your initial is: " + first_name_initial)
