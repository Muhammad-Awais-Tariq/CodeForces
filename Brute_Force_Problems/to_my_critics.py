import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    for _ in range(n):
        a, b , c = map(int, input().split())
        print("YES"  if a + b >= 10 or a + c >= 10 or b + c >= 10 else "No")


if __name__ == "__main__":
    solve()