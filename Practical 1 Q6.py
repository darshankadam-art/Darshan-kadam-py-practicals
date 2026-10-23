# Practical 1 - Q6: Implicit vs Explicit Type Conversion
number = 10
decimal = 2.5
print("int + float:", number + decimal)
print("Result type:", type(number + decimal))
try:
    print(number + "5")
except TypeError as error:
    print("Type error:", error)
print("After explicit casting:", number + int("5"))
print("String concatenation:", str(number) + "5")
