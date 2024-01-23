def door_mat_pattern(N, M):
    pattern = [('.|.' * (2 * i + 1)).center(M, '-') for i in range(N // 2)]
    welcome_line = 'WELCOME'.center(M, '-')
    mat_pattern = '\n'.join(pattern + [welcome_line] + pattern[::-1])
    return mat_pattern

# Input
N, M = map(int, input().split())

# Output
result = door_mat_pattern(N, M)
print(result)
