from itertools import combinations

def calculate_probability(n, letters, k):
    total_combinations = list(combinations(range(n), k))
    favorable_combinations = [comb for comb in total_combinations if 'a' not in [letters[i] for i in comb]]

    probability = len(favorable_combinations) / len(total_combinations)
    return round(1 - probability, 4)

# Read input
n = int(input().strip())
letters = input().strip().split()
k = int(input().strip())

# Calculate and print the probability
result = calculate_probability(n, letters, k)
print(result)
