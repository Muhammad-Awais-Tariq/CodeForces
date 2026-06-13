import sys
input = sys.stdin.readline

def solve():
    n = int(input().strip())

    while True:
        n = n + 1
        if len(set(str(n))) == len(str(n)):
            print(int(n))
            break
   
if __name__ == "__main__":
    solve()