# Accept three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Compare the three values
if a >= b and a >= c:
    # The first number is at least as large as both others
    largest = a
elif b >= a and b >= c:
    # The second number is at least as large as both others
    largest = b
else:
    # Otherwise, the third number is the largest
    largest = c

# Display the largest value
print("Largest number:", largest)
