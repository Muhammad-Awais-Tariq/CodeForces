import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    for _ in range(n):
        expression = input().strip()
        print(eval(expression))
        
if __name__ == "__main__":
    solve()