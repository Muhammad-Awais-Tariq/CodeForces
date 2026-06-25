
"""
Input an n x n matrix and determine whether it is symmetric.

A matrix is symmetric if:

matrix[i][j] == matrix[j][i]

for every valid i and j.

Example

Input:
3
1 2 3
2 4 5
3 5 6

Output:
Symmetric
"""


n = int(input())
matrix = []
is_symmetric = True

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    matrix.append(row)

for k in range(n):
    for l in range(n):
        if matrix[k][l] != matrix[l][k]:
            is_symmetric = False
            break
    if not is_symmetric:
        break

print("Symmetric" if is_symmetric else "Not Symmetric")