# Import NumPy
import numpy as np

# Create two matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# Perform matrix multiplication
product = A @ B

# Calculate the transpose of matrix A
transpose = A.T

# Display the matrices and results
print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

print("Matrix multiplication A @ B:")
print(product)

print("Transpose of A:")
print(transpose)

# Calculate matrix multiplication manually
manual = [
    [
        A[0, 0] * B[0, 0] + A[0, 1] * B[1, 0],
        A[0, 0] * B[0, 1] + A[0, 1] * B[1, 1]
    ],
    [
        A[1, 0] * B[0, 0] + A[1, 1] * B[1, 0],
        A[1, 0] * B[0, 1] + A[1, 1] * B[1, 1]
    ]
]

print("Manual multiplication:")
for row in manual:
    print(row)
