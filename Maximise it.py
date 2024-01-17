from itertools import product

def maximize_expression_value(arrays, modulo):
    # Generate all possible combinations of elements from the lists
    all_combinations = product(*arrays)
    
    # Calculate the value of the expression for each combination and find the maximum
    max_value = max(sum(x ** 2 for x in combination) % modulo for combination in all_combinations)
    
    return max_value

# Read input
n, m = map(int, input().split())
arrays = [list(map(int, input().split()[1:])) for _ in range(n)]

# Calculate and print the result
result = maximize_expression_value(arrays, m)
print(result)
