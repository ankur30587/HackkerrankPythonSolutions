import numpy as np

# Input: Reading space-separated integers for the shape of the array
shape = tuple(map(int, input().split()))

# Create an array of zeros with the specified shape and default type (float)
zeros_array = np.zeros(shape, dtype=int)
print(zeros_array)

# Create an array of ones with the specified shape and default type (float)
ones_array = np.ones(shape, dtype=int)
print(ones_array)
