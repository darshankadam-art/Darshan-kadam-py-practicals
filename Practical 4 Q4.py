# Accept a non-negative integer
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative integers.")
else:
    # Calculate factorial using a for loop
    fact_for = 1

    for i in range(1, n + 1):
        # Multiply the running factorial by each integer
        fact_for *= i

    # Calculate factorial using a while loop
    fact_while = 1
    i = 1

    while i <= n:
        # Multiply the running factorial by i
        fact_while *= i

        # Move to the next integer
        i += 1

    # Display both results for comparison
    print("Factorial using for loop:", fact_for)
    print("Factorial using while loop:", fact_while)
