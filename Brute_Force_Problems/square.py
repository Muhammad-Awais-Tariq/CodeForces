import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    for _ in range(n):
        a, b , c , d = map(int, input().split())
        print('YES' if a == b and b == c and c == d else "NO")
        
if __name__ == "__main__":
    solve()