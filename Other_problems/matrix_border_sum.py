
"""
Matrix Border Sum

Given an n x n matrix, calculate the sum of only the border elements.

Input
3
1 2 3
4 5 6
7 8 9

Output
40

Explanation:
1 2 3
4   6
7 8 9

Border sum = 1+2+3+4+6+7+8+9 = 40
"""

n = int(input())
matrix = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    matrix.append(row)

sum_matrix = 0

for i in range(n):
    for j in range(n):
        if i == 0:
            sum_matrix += matrix[i][j]
        elif i == n-1:
            sum_matrix += matrix[i][j]
        elif j == 0:
            sum_matrix += matrix[i][j]
        elif j == n-1:
            sum_matrix += matrix[i][j]
            

print(sum_matrix)