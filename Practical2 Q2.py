# Input without type conversion
a = input("Enter first number: ")
b = input("Enter second number: ")

print("Without conversion:")
print("Addition:", a + b)

# Input with type conversion
a = float(a)
b = float(b)

print("\nWith conversion:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Division is not possible by zero.")
