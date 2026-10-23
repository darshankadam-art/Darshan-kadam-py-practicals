# Accept an integer from the user
number = int(input("Enter an integer: "))

# Numbers less than 2 are not prime
if number < 2:
    print("The number is not prime.")
else:
    # Assume the number is prime until a divisor is found
    is_prime = True

    # Start checking possible divisors from 2
    divisor = 2

    # Check only up to the square root of the number
    while divisor * divisor <= number:
        if number % divisor == 0:
            # A zero remainder means the number is divisible
            is_prime = False
            break

        # Check the next possible divisor
        divisor += 1

    # Display the final result
    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")
