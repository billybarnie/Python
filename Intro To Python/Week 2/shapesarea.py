import math

# Area of a square
number = float(input("What is the length of a side of the square? "))
area = number * number
print(f"The area of the square is: {area:.2f}")

# Area of a rectangle
length = float(input("What is the length of a rectangle? "))
width = float(input("What is the width og a rectangle? "))
area1 = width * length
print(f"The area if the rectangle is: {area1}")

# Area of a circle
rad = float(input("What is the radius of the circle? "))
area3 = math.pi * rad * rad
print(f"The are of the circle is: {area3:.1f}")

# different areas of a circle
val = float(input("What is the value being used? "))
vol = val * val * val
volsph = (4/3) * math.pi * (val * val * val)

# volumes of both a cube and a sphere
print(f"The volume of a cube is: {vol:.1f}")
print(f"The volume of a sphere is: {volsph:.1f}")

# finding the area of the square in cm and transfering to meters based off the length of one of it's sides
number = float(input("What is the length of a side of the square in centimeters? "))
area = number * number
print(f"The area of the square would be: {area:.4f} centimeters squared")
print(f"The area of square in meters squared would be {area/ 10000:.4f}")

#Finding the area of the rectangle in cm and transfering to meters based off the length and width
length = float(input("What is the length of the rectangle in centimeters? "))
width = float(input("What is the width of the rectangle in centimeters? "))
area1 = width * length
print(f"The area of the rectangle would be: {area1:.4f} centimeters squared")
print(f"The area of the rectangle in meters squared would be: {area1/ 10000:.4f}")

# Finding the area of the circe in cm and transfering to meters based on the radius of the circle
rad = float(input("What is the radius of the circle in centimeters? "))
area3 = math.pi * rad * rad
print(f"The area of the circle in centimeters is: {area3:.4f}")
print(f"The area of the circle in meters squared would be: {area3/ 10000:.4f}")
