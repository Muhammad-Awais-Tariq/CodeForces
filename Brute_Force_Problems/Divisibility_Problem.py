import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        remainder = a % b

        if remainder == 0:
            print(0)
        else:
            print(b - remainder)
        
if __name__ == "__main__":
    solve()