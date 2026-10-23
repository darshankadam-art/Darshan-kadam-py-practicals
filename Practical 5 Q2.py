
# Loop through numbers from 1 to 10
for i in range(1, 11):
    # Skip the current iteration if i is divisible by 3
    if i % 3 == 0:
        continue

    # Print numbers that are not multiples of 3
    print(i, end=" ")

print()
