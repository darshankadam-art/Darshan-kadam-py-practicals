# Import NumPy
import numpy as np

# Create a dataset: each row represents a student
# Columns represent Physics, Chemistry, and Mathematics
marks = np.array([
    [85, 90, 88],
    [70, 75, 80],
    [95, 92, 96],
    [60, 65, 62]
])

# Define student names
students = ["Student 1", "Student 2", "Student 3", "Student 4"]

# Calculate the average marks for each student
averages = np.mean(marks, axis=1)

# Find the highest and lowest individual marks
highest = np.max(marks)
lowest = np.min(marks)

# Find the positions of the highest and lowest marks
highest_position = np.unravel_index(np.argmax(marks), marks.shape)
lowest_position = np.unravel_index(np.argmin(marks), marks.shape)

# Display each student's average
print("Average marks per student:")
for i in range(len(students)):
    print(f"{students[i]}: {averages[i]:.2f}")

# Display the highest and lowest marks
print("Highest mark:", highest)
print("Lowest mark:", lowest)

print(
    "Highest mark belongs to:",
    students[highest_position[0]]
)
print(
    "Lowest mark belongs to:",
    students[lowest_position[0]]
)
