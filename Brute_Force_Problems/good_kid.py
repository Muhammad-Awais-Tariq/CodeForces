import sys
import math
input = sys.stdin.readline

def solve():
    n = int(input())
    for _ in range(n):
        no_of_integers = int(input())
        arr = list(map(int , input().split()))
        arr.sort()
        arr[0] = arr[0] + 1
        print(math.prod(arr))


if __name__ == "__main__":
    solve()