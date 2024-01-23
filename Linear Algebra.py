import numpy as np

# Read the size of the matrix
n = int(input())

# Read the matrix elements
matrix = [list(map(float, input().split())) for _ in range(n)]

# Calculate the determinant
determinant = np.linalg.det(matrix)

# Round the determinant to 2 decimal places
rounded_determinant = round(determinant, 2)

# Print the result
print(rounded_determinant)
