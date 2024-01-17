from itertools import combinations

s, k = input().split()
letters = sorted(s)

for i in range(1, int(k) + 1):
    # Use sorted(combinations(...)) to ensure lexicographic order
    for combination in sorted(combinations(letters, i)):
        print("".join(combination))
