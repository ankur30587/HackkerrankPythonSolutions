import numpy as np

# Read coefficients of the polynomial
coefficients = list(map(float, input().split()))

# Read the value of x
x = float(input())

# Evaluate the polynomial at x
result = np.polyval(coefficients, x)

# Print the result
print(result)
