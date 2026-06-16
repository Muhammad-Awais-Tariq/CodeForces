import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    for _ in range(n):
        arr = list(input().strip())
        first_3_sum = sum(map(int ,arr[:3]))
        last_3_sum = sum(map(int ,arr[3:]))
        print("YES" if first_3_sum == last_3_sum else "NO")

if __name__ == "__main__":
    solve()