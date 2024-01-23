import numpy as np

# Input: Reading values for rows and columns
rows, columns = map(int, input().split())

# Set the printing option for numpy
np.set_printoptions(sign=' ')

# Create the desired array using numpy.eye
result_array = np.eye(rows, columns)

# Print the result array
print(result_array)
