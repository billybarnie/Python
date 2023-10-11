import math

def compute_area_square(user):
    area = user * 2
    return area

def compute_area_rectangle(length, width):
    area = width * length
    return area

def compute_area_circle(radius):
    area = math.pi * (radius * 2)
    return area

def compute_area(object, piece_one, piece_two=0):
    area = -1
    
    if object == "square":
        area = compute_area_square(piece_one)
    elif object == "rectangle": 
        area = compute_area_rectangle(piece_one, piece_two)
    elif object == "circle":
        area = compute_area_circle(piece_one)

    return area

object = ""

print("You are able to find the areas of a circle, rectangle, or square in this program.\
 When you are finished with the program just type 'quit' to exit.")
print()

while object != "quit":
    object = input("What shape do you have? ")
    object = object.lower()

    if object == "square":
        print()
        user = float(input("What is the length of a side of the square? "))
        area = compute_area(object, user)
        print(f"The area of the square is: {area:.3f}")
        print()
    elif object == "rectangle":
        print()
        length = float(input("What is the length of a rectangle? "))
        width = float(input("What is the width of a rectangle? "))
        area = compute_area(object, length, width)
        print(f"The area of the rectangle is: {area:.3f}")
        print()
    elif object == "circle":
        print()
        radius = float(input("What is the radius of the circle? "))
        area = compute_area(object, radius)
        print(f"The area of the circle is: {area:.3f}")
        print()