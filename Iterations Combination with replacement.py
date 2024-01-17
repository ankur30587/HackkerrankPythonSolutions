from itertools import combinations_with_replacement

s, k = input().split()
letters = sorted(s)

# Use sorted(combinations_with_replacement(...)) to ensure lexicographic order
for combination in sorted(combinations_with_replacement(letters, int(k))):
    print("".join(combination))