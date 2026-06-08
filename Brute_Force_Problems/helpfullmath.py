import sys
input = sys.stdin.readline

def solve():
    equ = input().strip().split("+")
    equ.sort()
    print("+".join(x for x in equ))

if __name__ == "__main__":
    solve()