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