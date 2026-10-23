# Accept numbers separated by spaces
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Accept the number to search for
target = int(input("Enter number to search: "))

found = False

# Search each number in the list
for i in range(len(numbers)):
    # Check whether the current element matches the target
    if numbers[i] == target:
        found = True

        # Display the position using 1-based numbering
        print("Number found at position:", i + 1)

        # Stop searching once the number is found
        break

# Display a message if the number is absent
if not found:
    print("Number not found.")
