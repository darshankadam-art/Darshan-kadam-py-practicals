# Import NumPy
import numpy as np

# Create an array of numbers
data = np.array([10, 20, 30, 40, 50])

# Calculate the mean, median, and standard deviation
mean_value = np.mean(data)
median_value = np.median(data)
std_value = np.std(data)

# Display the results
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard deviation:", round(std_value, 2))
