print("Please enter the following information: ")
print()                             # Separater
First = input("First name: ")       # This asks for the users first name
Last = input("Last name: ")         # This asks for the users last name
email = input("Email address: ")    # This asks the user for their email
num = input("Phone number: ")       # This asks the user for their phone number
job = input("Job title: ")          # This asks the user for their job title
id = input("ID Number: ")           # This asks the user for their personal Identification number
hair = input("Hair color: ")        # This asks the user for their hair color
eyes = input("Eye color: ")         # This asks the user for their eye color
birthday = input("Date of Birth: ") # This asks the user for their date of birth
train = input("Training: ")         # This asks the user if they are currently in training
print()                             # Separater

# the following prints out the users inputs as appropiate for the ID card
print("The ID Card is: ")
print("-----------------------------------------")  # Separater 
print(f"{Last.upper()}, {First.capitalize()}")
print(f"{job.title()}")
print(f"ID: {id}")
print()
print(f"{email}")
print(f"{num}")
print()
print(f"Hair: {hair.capitalize():20}Eyes: {eyes.capitalize()}")
print(f"Birth Date: {birthday:14}Training: {train.capitalize()}")
print("-----------------------------------------")  # Separater