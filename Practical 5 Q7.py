# Initialize the sum
total = 0

while True:
    # Accept a number from the user
    number = int(input("Enter a number (0 to stop): "))

    # Stop the loop when the input is zero
    if number == 0:
        break

    # Ignore negative numbers
    if number < 0:
        print("Negative number ignored.")
        continue

    # Add valid positive numbers to the total
    total += number

# Display the final sum
print("Sum of valid inputs:", total)
