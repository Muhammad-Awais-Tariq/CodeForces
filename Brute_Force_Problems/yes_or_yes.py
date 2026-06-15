import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    for _ in range(n):
        print("YES" if input().lower().strip() == "yes" else "NO")

if __name__ == "__main__":
    solve()