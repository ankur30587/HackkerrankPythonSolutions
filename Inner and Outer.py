import numpy as np

# Read input arrays
A = np.array(input().split(), dtype=int)
B = np.array(input().split(), dtype=int)

# Compute inner product
inner_product = np.inner(A, B)

# Compute outer product
outer_product = np.outer(A, B)

# Print the results
print(inner_product)
print(outer_product)
