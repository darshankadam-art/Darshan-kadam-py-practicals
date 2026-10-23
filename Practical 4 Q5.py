# Accept the number from the user
number = int(input("Enter a number: "))

# Print the multiplication table heading
print(f"Multiplication Table of {number}")

# Repeat from 1 to 10
for i in range(1, 11):
    # Multiply the number by the current multiplier
    result = number * i

    # Display the calculation neatly
    print(f"{number} x {i} = {result}")
