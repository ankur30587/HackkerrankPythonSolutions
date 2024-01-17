from collections import defaultdict

def word_indices(group_a_size, group_b_size, group_a, group_b):
    group_a_indices = defaultdict(list)

    for i in range(1, group_a_size + 1):
        word = group_a[i - 1]
        group_a_indices[word].append(i)

    for j in range(group_a_size + 1, group_a_size + group_b_size + 1):
        word = group_b[j - group_a_size - 1]
        indices = group_a_indices[word]
        if indices:
            print(" ".join(map(str, indices)))
        else:
            print(-1)

# Read input sizes
group_a_size, group_b_size = map(int, input().split())

# Read group A and group B
group_a = [input().strip() for _ in range(group_a_size)]
group_b = [input().strip() for _ in range(group_b_size)]

# Calculate and print the result
word_indices(group_a_size, group_b_size, group_a, group_b)
