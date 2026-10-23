# Practical 1 - Q11: Temperature Converter
try:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
except ValueError:
    print("Invalid input: please enter a numeric temperature.")
