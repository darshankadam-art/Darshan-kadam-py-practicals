# Define the first matrix
A = [
    [1, 2, 3],
    [4, 5, 6]
]

# Define the second matrix
B = [
    [7, 8, 9],
    [10, 11, 12]
]

# Get the number of rows and columns
rows = len(A)
columns = len(A[0])

# Create an empty result matrix
result = []

# Add corresponding elements using nested loops
for i in range(rows):
    row = []

    for j in range(columns):
        # Add the elements at the same position
        row.append(A[i][j] + B[i][j])

    # Add the completed row to the result
    result.append(row)

# Display the result matrix
print("Result of matrix addition:")
for row in result:
    print(row)
