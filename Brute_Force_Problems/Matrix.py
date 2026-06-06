import sys
input = sys.stdin.readline

def solve():
    matrix = [] 
    for i in range(5): 
        n = list(map(int , input().strip().split(" "))) 
        matrix.append(n) 

    for i in range(5): 
        for j in range(5): 
            if matrix[i][j] == 1:
                n = abs(i - 2) + abs(j - 2)
                print(n) 
                break

if __name__ == "__main__":
    solve()