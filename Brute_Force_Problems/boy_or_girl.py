import sys
input = sys.stdin.readline

def solve():
    n = input().strip()

    if len(set(n)) % 2 != 0:
        print("IGNORE HIM!")
    else:
        print("CHAT WITH HER!")

if __name__ == "__main__":
    solve()