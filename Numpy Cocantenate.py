import numpy as np

# Input: Reading values for rows, columns, and axis
a, b, axis = map(int, input().split())

# Reading the elements of the first array
arr1 = np.array([input().split() for _ in range(a)], dtype=int)

# Reading the elements of the second array
arr2 = np.array([input().split() for _ in range(b)], dtype=int)

# Concatenate the arrays along the specified axis
result_array = np.concatenate((arr1, arr2))

# Print the concatenated array
print(result_array)
