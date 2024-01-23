import numpy as np

# Input: Reading values for rows and columns
rows, columns = map(int, input().split())

# Reading the elements of the array
matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Convert the list of lists into a NumPy array
my_array = np.array(matrix)

# Print the transpose array
transpose_array = np.transpose(my_array)
print(transpose_array)

# Print the flattened array
flatten_array = my_array.flatten()
print(flatten_array)
