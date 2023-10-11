import math

number = int(input("Enter the number of items: "))
per_box = int(input("Enter the number of items per box: "))

box = math.ceil(number / per_box)

print(f"For {number} items, packing {per_box} items in each box, you will need {box} boxes.")

