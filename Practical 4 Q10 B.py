# Print the heading
print("Increasing Number Pattern:")

# Control the number of rows
for i in range(1, 5):
    # Print numbers from 1 up to the current row number
    for j in range(1, i + 1):
        print(j, end=" ")

    # Move to the next row
    print()
