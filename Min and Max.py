import numpy as np

# Input: Reading values for rows and columns
rows, columns = map(int, input().split())

# Reading the elements of the 2-D array
my_array = np.array([input().split() for _ in range(rows)], int)

# Compute the min along axis 1
min_result = np.min(my_array, axis=1)

# Print the max of the min result
result = np.max(min_result)
print(result)
