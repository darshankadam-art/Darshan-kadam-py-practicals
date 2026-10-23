# Accept two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Accept the required arithmetic operator
operator = input("Enter operator (+, -, *, /): ")

# Perform the operation according to the operator
if operator == "+":
    result = a + b
    print("Result:", result)
elif operator == "-":
    result = a - b
    print("Result:", result)
elif operator == "*":
    result = a * b
    print("Result:", result)
elif operator == "/":
    # Division by zero must be prevented
    if b != 0:
        result = a / b
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    # Handle an operator not supported by the calculator
    print("Invalid operator.")
