import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    for _ in range(n):
        a , b , c, d = map(int , input().split())
        if b > a and c > a and d > a:
            print(3)
        elif b > a and c > a or d > a and c > a or b > a and d > a:
            print(2)
        elif b > a or c > a or d > a:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    solve()