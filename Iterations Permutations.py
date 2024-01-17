from itertools import permutations

input_str, size = input().split()
size = int(size)

result = sorted(permutations(input_str, size))
for item in result:
    print(''.join(item))
