# Import NumPy
import numpy as np

# Create a one-dimensional array containing 12 elements
arr = np.arange(1, 13)

# Display the original array
print("Original 1D array:")
print(arr)

# Reshape the array into 3 rows and 4 columns
arr_3x4 = arr.reshape(3, 4)
print("\nReshaped 3 x 4 array:")
print(arr_3x4)

# Reshape the same array into 2 rows and 6 columns
arr_2x6 = arr.reshape(2, 6)
print("\nReshaped 2 x 6 array:")
print(arr_2x6)

# Demonstrate an invalid reshape
try:
    arr.reshape(5, 3)
except ValueError:
    print("\nError: Cannot reshape 12 elements into a 5 x 3 array.")
