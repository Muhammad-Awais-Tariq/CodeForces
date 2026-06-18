import sys
input = sys.stdin.readline

def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        longest = 0
        current = 0

        for num in arr:
            if num == 0:
                current += 1
                longest = max(longest, current)
            else:
                current = 0

        print(longest)

if __name__ == "__main__":
    solve()