# Accept numbers separated by spaces
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Positive numbers:")

# Examine each number in the list
for number in numbers:
    # Skip negative numbers
    if number < 0:
        continue

    # Print positive numbers only
    if number > 0:
        print(number, end=" ")

print()
