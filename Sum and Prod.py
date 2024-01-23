import numpy as np

# Input: Reading values for rows and columns
rows, columns = map(int, input().split())

# Reading the elements of the 2-D array
my_array = np.array([input().split() for _ in range(rows)], int)

# Compute the sum along axis 0
sum_result = np.sum(my_array, axis=0)

# Print the product of the sum
result = np.prod(sum_result)
print(result)
