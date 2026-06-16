import sys
input = sys.stdin.readline

def solve():

    n = int(input())
    for _ in range(n):
        a , b ,c = map(int , input().split())
        if a == b:
            print(c)
        elif b == c:
            print(a)
        else:
            print(b)


if __name__ == "__main__":
    solve()