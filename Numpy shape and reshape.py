import numpy as np

# Input: Reading space-separated numbers and creating a NumPy array
numbers = input().strip().split()
numpy_array = np.array(numbers, int)  # Converting to NumPy array with integer type

# Reshape the array into a 3x3 matrix
result_array = np.reshape(numpy_array, (3, 3))

# Print the X NumPy array
print(result_array)
