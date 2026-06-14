import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    print("YES" if len(set(input().lower().strip())) == 26 else "NO")

if __name__ == "__main__":
    solve()