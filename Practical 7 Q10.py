
# Create an original list
numbers_list = [10, 20, 30]

# Convert the list into a tuple
numbers_tuple = tuple(numbers_list)
print("List converted to tuple:", numbers_tuple)

# Create a tuple and convert it into a list
values_tuple = (40, 50, 60)
values_list = list(values_tuple)
print("Tuple converted to list:", values_list)

# Modify the converted list
values_list[0] = 99
values_list.append(70)
print("Modified list:", values_list)

# The original tuple remains unchanged
print("Original tuple:", values_tuple)
