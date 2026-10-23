
# Create a 3 x 3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Traverse the matrix row-wise
print("Row-wise traversal:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        # Print elements from left to right in each row
        print(matrix[i][j], end=" ")
    print()

# Traverse the matrix column-wise
print("Column-wise traversal:")
for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        # Keep the column fixed and change the row
        print(matrix[i][j], end=" ")
    print()
