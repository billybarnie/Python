import math
from datetime import datetime

user = ""

while user != "no":
    width = input("Enter the width of the tire in mm (ex 205): ")
    ratio = input("Enter the aspect ratio of the tire (ex 60): ")
    diameter = input("Enter the diameter of the wheel in inches (ex 15): ")
    w = int(width)
    a = int(ratio)
    d = int(diameter)

    v = (math.pi * w * w * a * (w * a + 2540 * d)) / 10000000000

    time = datetime.now()
    print(f"The approximate volume is {v:.2f} liters")
    print()
    with open("volumes.txt", "at") as volumesfile:
        print(f"{time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {v:.2f}", file=volumesfile)
    volumesfile.close()

    user = input("Would you like to find other tire volumes? (yes/no): ")
    if user == "yes":
        print()
    else:
        print()
        print("Have a beautiful day!")