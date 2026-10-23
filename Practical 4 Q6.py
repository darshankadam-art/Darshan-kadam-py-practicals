# Accept a non-negative integer
number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Please enter a non-negative integer.")
else:
    # Preserve the original number for comparison
    original = number

    # Initialize the reversed number
    reverse = 0

    # Extract digits until the number becomes zero
    while number > 0:
        digit = number % 10

        # Shift the existing digits left and append the last digit
        reverse = reverse * 10 + digit

        # Remove the last digit from the original number
        number //= 10

    # Display the reversed number
    print("Reversed number:", reverse)

    # Compare the original and reversed values
    if original == reverse:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
