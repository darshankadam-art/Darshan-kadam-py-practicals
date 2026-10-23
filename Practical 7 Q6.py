
# Create a list of numbers
numbers = [10, 20, 30, 40, 50]

# Remove the specified value
numbers.remove(30)
print("After remove(30):", numbers)

# Remove and return the last element
removed = numbers.pop()
print("Popped element:", removed)
print("After pop():", numbers)

# Handle an element that does not exist
try:
    numbers.remove(100)
except ValueError:
    print("Error: 100 is not present in the list.")

# Handle an invalid pop index
try:
    numbers.pop(10)
except IndexError:
    print("Error: The specified index does not exist.")
