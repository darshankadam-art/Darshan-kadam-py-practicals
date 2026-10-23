
# Create a list and a tuple
numbers_list = [10, 20, 30]
numbers_tuple = (10, 20, 30)

# Modify an element in the list
numbers_list[1] = 99
print("Modified list:", numbers_list)

# Attempt to modify an element in the tuple
try:
    numbers_tuple[1] = 99
except TypeError as error:
    print("Tuple modification error:", error)

# Display the original tuple
print("Original tuple:", numbers_tuple)
