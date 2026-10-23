
# Create a numeric list and a numeric tuple
numbers_list = [10, 20, 30, 40, 50]
numbers_tuple = (10, 20, 30, 40, 50)

# Iterate through the list
print("List elements:")
for number in numbers_list:
    print(number, end=" ")

# Calculate the sum of the list
total = 0
for number in numbers_list:
    total += number

print("\nSum of list:", total)

# Iterate through the tuple
print("Tuple elements:")
for number in numbers_tuple:
    print(number, end=" ")

print()
