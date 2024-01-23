import numpy as np

# Set the printing option for numpy
np.set_printoptions(sign=' ')

# Input: Reading the elements of the array
my_array = np.array(input().split(), float)

# Print the floor, ceil, and rint of the array
print(np.floor(my_array))
print(np.ceil(my_array))
print(np.rint(my_array))
