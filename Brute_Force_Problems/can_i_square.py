import sys
input = sys.stdin.readline

def solve():
    total_iteration = int(input())
    for _ in range(total_iteration):
        total_square = int(input())
        sum_squares = sum(list(map(int, input().split())))
        square_root = sum_squares ** 0.5
        print("YES" if (sum_squares % square_root) == 0.0 else "NO")

if __name__ == "__main__":
    solve()