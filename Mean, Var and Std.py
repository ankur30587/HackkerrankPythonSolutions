import numpy as np

# Input: Reading values for rows and columns
N, M = map(int, input().split())

# Reading the elements of the 2-D array
arr = np.array([input().split() for _ in range(N)], dtype=int)

# Compute the mean, var, and std along axis 0
mean_result = np.mean(arr, axis=1)
var_result = np.var(arr, axis=0)
std_result = np.std(arr)

# Print the results
print(mean_result)
print(var_result)
print(round(std_result, 11))
