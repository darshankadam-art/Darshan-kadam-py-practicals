
# Create the original list
numbers = [40, 10, 50, 20, 30]
print("Original list:", numbers)

# Sort in ascending order
ascending = numbers.copy()
ascending.sort()
print("Ascending order:", ascending)

# Sort in descending order
descending = numbers.copy()
descending.sort(reverse=True)
print("Descending order:", descending)

# Reverse the original order without sorting
reversed_list = numbers.copy()
reversed_list.reverse()
print("Reversed list:", reversed_list)
