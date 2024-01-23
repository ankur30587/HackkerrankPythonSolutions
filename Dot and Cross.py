import numpy as np

# Input: Reading the value of N
N = int(input())

# Reading the elements of the first array
arr1 = np.array([input().split() for _ in range(N)], dtype=int)

# Reading the elements of the second array
arr2 = np.array([input().split() for _ in range(N)], dtype=int)

# Compute the matrix product
result = np.dot(arr1, arr2)

# Print the result
print(result)
