import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    for _ in range(n):
        arr = list(map(int, input().split()))
        sorted_number = sorted(arr)
        print(sorted_number[1])
        
if __name__ == "__main__":
    solve()