# Ask how many numbers will be entered
n = int(input("How many numbers do you want to enter? "))

# Initialize the sum to zero
total = 0

# Check that at least one number will be entered
if n <= 0:
    print("Please enter a positive count.")
else:
    # Repeat n times to accept the numbers
    for i in range(1, n + 1):
        number = float(input(f"Enter number {i}: "))

        # Add each number to the running total
        total += number

    # Calculate the average
    average = total / n

    # Display the results
    print("Sum:", total)
    print("Average:", average)
