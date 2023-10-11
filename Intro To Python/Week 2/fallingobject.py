import math

# Introductary for the velocity calculator
print("Welcome to the velocity calculator. Please enter the following: ")
print()

# Gathering inputs for velocity from user
m = float(input("Mass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
a = float(input("Cross sectional area (in m^2): "))
c = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
print()

#formulas
C = (1/2) * p * a * c
v = math.sqrt(m * g / C) * (1 - math.exp((-math.sqrt(m * g * C) / m) * t))

# shows the output of what the user entered for the velocity calculations
print(f"The inner value of c is: {C:.3f}")
print(f"The velocity after {t} seconds is: {v:.3f} m/s")
print()

