import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    target = sorted("Timur")
    for _ in range(n):
        size = int(input())
        string = input().strip()
        if size == 5 and sorted(string) == target:
            print("YES")
        else:
            print("No")

if __name__ == "__main__":
    solve()