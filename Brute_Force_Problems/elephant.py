import sys
input = sys.stdin.readline
import math

def solve():
    n = int(input())
    steps = math.ceil(n/5)
    print(steps)
    

if __name__ == "__main__":
    solve()