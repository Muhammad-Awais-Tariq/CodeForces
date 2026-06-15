import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    for _ in range(n):
        x , y , z = map(int, input().strip().split())

        print("YES" if x + y == z or x + z == y or y + z == x else "NO")
        
if __name__ == "__main__":
    solve()