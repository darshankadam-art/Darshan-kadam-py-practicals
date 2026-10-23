# Define a sample 3 x 3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
columns = len(matrix[0])

# Calculate the sum of each row
print("Row sums:")
for i in range(rows):
    row_sum = 0

    for j in range(columns):
        # Add each element in the current row
        row_sum += matrix[i][j]

    print(f"Row {i + 1}: {row_sum}")

# Calculate the sum of each column
print("Column sums:")
for j in range(columns):
    column_sum = 0

    for i in range(rows):
        # Add each element in the current column
        column_sum += matrix[i][j]

    print(f"Column {j + 1}: {column_sum}")
