# Accept a non-negative integer
number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Please enter a non-negative integer.")
else:
    # Convert the number to text to count its digits easily
    digits = str(number)

    # Initialize all counters
    total_digits = 0
    even_digits = 0
    odd_digits = 0

    # Examine each digit in the number
    for ch in digits:
        digit = int(ch)

        # Count every digit
        total_digits += 1

        # Classify the digit as even or odd
        if digit % 2 == 0:
            even_digits += 1
        else:
            odd_digits += 1

    # Display the counters
    print("Total digits:", total_digits)
    print("Even digits:", even_digits)
    print("Odd digits:", odd_digits)
