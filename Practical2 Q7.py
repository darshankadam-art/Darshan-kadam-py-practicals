km = float(input("Enter distance in kilometres: "))
celsius = float(input("Enter temperature in Celsius: "))
rupees = float(input("Enter amount in rupees: "))

meters = km * 1000
fahrenheit = (celsius * 9 / 5) + 32
dollars = rupees / 83

print(f"Distance: {meters:.2f} metres")
print(f"Temperature: {fahrenheit:.2f} Fahrenheit")
print(f"Amount: ${dollars:.2f}")
