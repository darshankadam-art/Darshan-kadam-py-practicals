
# Create a 3 x 3 matrix using nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Display the entire matrix
print("Entire matrix:")
for row in matrix:
    print(row)

# Display the first row (index 0)
print("First row:", matrix[0])

# Display the element at row 2, column 3
# Python uses zero-based indexing, so use matrix[1][2]
print("Element at (2, 3):", matrix[1][2])
