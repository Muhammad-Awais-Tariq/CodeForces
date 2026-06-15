import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    all_levels = set(arr1[1:] + arr2[1:])
    print("I become the guy." if len(all_levels) == n else "Oh, my keyboard!")

if __name__ == "__main__":
    solve()