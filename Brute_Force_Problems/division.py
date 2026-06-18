import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    for _ in range(n):
        value = int(input())

        if value >= 1900:
            print("Division 1")
        elif 1899 >= value >= 1600:
            print("Division 2")
        elif 1599 >= value >= 1400:
            print("Division 3")
        else:
            print("Division 4")

if __name__ == "__main__":
    solve()