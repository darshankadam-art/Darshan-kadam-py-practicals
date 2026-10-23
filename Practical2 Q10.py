# Error 1: Division by zero
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Error 2: Adding a string and an integer
try:
    result = "10" + 5
    print(result)
except TypeError:
    print("Error: Cannot add a string and an integer.")

# Corrected expressions
print("Correct division:", 10 / 2)
print("Correct addition:", int("10") + 5)
