# Print a pattern with three rows
for i in range(1, 4):
    # Examine numbers from 1 through the current row number
    for j in range(1, i + 1):
        # Skip even numbers
        if j % 2 == 0:
            continue

        # Print only odd numbers
        print(j, end=" ")

    # Start a new row
    print()
