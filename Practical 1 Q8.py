# Practical 1 - Q8: Swapping Variables Using Multiple Methods
# Method 1: temporary variable
a = 10
b = 20
print("Before swap (method 1):", a, b)
temp = a
a = b
b = temp
print("After swap (method 1):", a, b)

# Method 2: tuple unpacking
x = 10
y = 20
print("Before swap (method 2):", x, y)
x, y = y, x
print("After swap (method 2):", x, y)
