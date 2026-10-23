# Create a 2 x 3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(matrix)
columns = len(matrix[0])

# Create an empty matrix with reversed dimensions
transpose = []

# Build the transpose by selecting one column at a time
for j in range(columns):
    new_row = []

    for i in range(rows):
        # Element at row i, column j becomes row j, column i
        new_row.append(matrix[i][j])

    transpose.append(new_row)

# Display the original matrix
print("Original matrix:")
for row in matrix:
    print(row)

# Display the transposed matrix
print("Transposed matrix:")
for row in transpose:
    print(row)
