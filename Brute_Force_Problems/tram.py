import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    max_capacity = 0 # maximum capcity that train need meaning the maximum number of passenger on the train
    temp_max = 0 # it contains the number of passenger on the train at a specific time
    for i in range(n):
        i , j = map(int , input().split())
        temp_max = (temp_max - i) + j
        max_capacity = max(max_capacity , temp_max)
    print(max_capacity)

if __name__ == "__main__":
    solve()