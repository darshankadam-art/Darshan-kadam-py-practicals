# Accept the number of Fibonacci terms
n = int(input("Enter the number of terms: "))

if n < 0:
    print("Please enter a non-negative number of terms.")
else:
    # Initialize the first two Fibonacci values
    a = 0
    b = 1

    print("Fibonacci Series:")

    # Generate the requested number of terms
    for i in range(n):
        # Print the current term
        print(a, end=" ")

        # Update both values using the previous pair
        a, b = b, a + b

    print()
