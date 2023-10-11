user_input = float(input("What is the temperature? "))

f_c = input("Fahrenheit or Celsius (F/C)? ")
f_c = f_c.lower()
T = user_input
fahr = 0.0
V = 1.61

def temp_formula(T, V):
    calculate_wind_chill = 35.74 + 0.6215 * T - 35.75 * (V ** 0.16) + 0.4275 * T * (V ** 0.16)
    return calculate_wind_chill

def f2c_formula(user_input):
    f2c = (user_input * 9/5) + 32
    return f2c

if f_c == "c":
    fahr = f2c_formula(user_input)
else: 
    fahr = user_input


for V in range(5, 65, 5):
    print(f"At temperature: {fahr}F, the wind speed {V} mph, the windchill is: {temp_formula(fahr, V):.2f}F")
 

