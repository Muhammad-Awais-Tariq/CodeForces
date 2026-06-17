import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    for _ in range(n):
        a, b , c = map(int, input().split())

        print("+" if a + b == c else "-")


if __name__ == "__main__":
    solve()