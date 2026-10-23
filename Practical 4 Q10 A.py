# Print an increasing star pattern
print("Increasing Star Pattern:")

for i in range(1, 5):
    # Print i stars on the current row
    for j in range(i):
        print("*", end="")

    # Move to the next line after each row
    print()

# Print a decreasing star pattern
print("\nDecreasing Star Pattern:")

for i in range(4, 0, -1):
    # Print i stars on the current row
    for j in range(i):
        print("*", end="")

    # Move to the next line after each row
    print()
