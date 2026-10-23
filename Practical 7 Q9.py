
# Create a nested list representing a 3 x 3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access an element using row and column indexes
print("Element at row 2, column 3:", matrix[1][2])

# Display the original matrix
print("Original matrix:")
for row in matrix:
    print(row)

# Modify the element at row 2, column 3
matrix[1][2] = 60

# Display the updated matrix
print("Updated matrix:")
for row in matrix:
    print(row)
