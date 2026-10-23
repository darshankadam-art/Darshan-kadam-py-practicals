# Import NumPy
import numpy as np

# Create two NumPy arrays
A = np.array([10, 20, 30])
B = np.array([1, 2, 3])

# Perform element-wise arithmetic operations
print("Addition:", A + B)
print("Subtraction:", A - B)
print("Multiplication:", A * B)

# Compare with Python lists
list_A = [10, 20, 30]
list_B = [1, 2, 3]

# Python lists do not perform element-wise addition
print("List concatenation:", list_A + list_B)

# Element-wise addition using a list comprehension
list_sum = [a + b for a, b in zip(list_A, list_B)]
print("List element-wise addition:", list_sum)
