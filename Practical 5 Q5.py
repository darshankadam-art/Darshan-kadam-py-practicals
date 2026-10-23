# Accept the divisor
n = int(input("Enter a positive number: "))

if n <= 0:
    # The divisor must be positive
    print("Please enter a positive number.")
else:
    # Search numbers from 1 through 100
    for i in range(1, 101):
        # Check whether i is divisible by n
        if i % n == 0:
            print("First divisible number:", i)

            # Stop after finding the first match
            break
    else:
        # This runs if the loop finishes without finding a match
        print("No divisible number found between 1 and 100.")
