import numpy as np

# Input: Reading values for X and Y
X, Y = map(int, input().split())

# Reading the elements of the first array
arr1 = np.array([input().split() for _ in range(X)], int)

# Reading the elements of the second array
arr2 = np.array([input().split() for _ in range(X)], int)

# Perform the specified operations
print(np.add(arr1, arr2))
print(np.subtract(arr1, arr2))
print(np.multiply(arr1, arr2))
print(np.floor_divide(arr1, arr2))  # Use floor_divide for integer division
print(np.mod(arr1, arr2))
print(np.power(arr1, arr2))
