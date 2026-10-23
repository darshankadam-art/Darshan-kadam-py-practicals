# Import NumPy
import numpy as np

# Create a 3 x 3 NumPy array
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Access the element at row 2, column 3
print("Specific element:", arr[1, 2])

# Access the entire second row
print("Second row:", arr[1, :])

# Access the entire second column
print("Second column:", arr[:, 1])

# Slice the first two rows and first two columns
print("Sliced array:")
print(arr[0:2, 0:2])
