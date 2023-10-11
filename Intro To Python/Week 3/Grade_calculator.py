print("This is a Grade calculator. Please enter your grade percentage in the following area below: ")
print()
grade = int(input("What is the grade percentage? "))

if grade >= 95:
    print("You have an A in the class. Great job!!")
elif grade >= 90:
    print("You have a A- in the class. Good work!!")
elif grade >= 85:
    print("You have a B+ in the class. Nice thats good!!")
elif grade >= 80:
    print("You have a B- in the class. Awesome!!")
elif grade >= 75:
    print("You have a C+ in the class. Great!!")
elif grade >= 70:
    print("You have a C- in the class. Nice!!")
elif grade >= 65:
    print("You have a D+ in the class. Please don't afraid to ask questions.")
elif grade >= 60:
    print("You have a D- in the class. Please don't be afraid to ask questions.")
else:
    print("You have an F in the class. You are in danger of failing the class, try to study a little bit more and ask questions if needed.")