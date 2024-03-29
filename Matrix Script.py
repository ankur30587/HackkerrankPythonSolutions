#!/bin/python3
n, m = map(int, input().rstrip().split())
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

sym = ('!', '@', '#', '$', '%', '&', ' ')
for i in matrix:
    while len(i) < m:
        i += ' '
decode = ''.join(matrix[i][j] for j in range(m) for i in range(n))
k = len(decode) - 1
h = 0
while k > -1 and decode[k] in sym:
    k -= 1
while h < len(decode) and decode[h] in sym:
    h += 1
part = decode[h : k+1]
for x in sym:
    part = part.replace(x, ' ')
while h >= len(decode) and k <= -1:
    k = h - 1
result = decode[:h] + ' '.join(_ for _ in part.split()) + decode[k+1:]
print(result)