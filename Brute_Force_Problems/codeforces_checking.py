import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    for _ in range(n):
        letter = input().strip().lower()
        print("YES" if letter in "codeforces" else "NO")


if __name__ == "__main__":
    solve()