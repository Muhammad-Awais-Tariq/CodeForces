import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    
    prev = input().strip()
    groups = 1

    for _ in range(n - 1):
        curr = input().strip()
        if curr != prev:
            groups += 1
        prev = curr

    print(groups)

if __name__ == "__main__":
    solve()