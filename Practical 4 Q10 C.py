# Print the heading
print("Reverse Number Pattern:")

# Start with four numbers and reduce the row size
for i in range(4, 0, -1):
    # Print numbers from 1 to i
    for j in range(1, i + 1):
        print(j, end=" ")

    # Move to the next row
    print()
