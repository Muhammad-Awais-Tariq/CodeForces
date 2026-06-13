import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    results = list(map(int , input().split()))

    if 1 in results:
        print("HARD")
    else:
        print("EASY")


if __name__ == "__main__":
    solve()