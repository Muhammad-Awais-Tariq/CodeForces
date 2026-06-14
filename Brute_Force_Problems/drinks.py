import sys
import math
input = sys.stdin.readline

def solve():
    n = int(input())
    numbers = list(map(int , input().split()))

    print(f"{math.fsum(numbers)/n:.12f}")
    
if __name__ == "__main__":
    solve()