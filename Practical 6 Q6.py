# Import the NumPy library
import numpy as np

# Create an array from a Python list
arr1 = np.array([10, 20, 30, 40])

# Create a 2 x 3 array filled with zeros
arr2 = np.zeros((2, 3))

# Create a 2 x 3 array filled with ones
arr3 = np.ones((2, 3))

# Display the first array
print("Array using np.array():")
print(arr1)
print("Shape:", arr1.shape)
print("Data type:", arr1.dtype)

# Display the zero array
print("\nArray using np.zeros():")
print(arr2)
print("Shape:", arr2.shape)
print("Data type:", arr2.dtype)

# Display the one array
print("\nArray using np.ones():")
print(arr3)
print("Shape:", arr3.shape)
print("Data type:", arr3.dtype)
