import sys
input = sys.stdin.readline

"""
You are given four distinct integers a, b, c, d.

Timur and three other people are running a marathon. The value a is the distance that Timur has run and b, c, d correspond to the distances the other three participants ran.

Output the number of participants in front of Timur.

Input
The first line contains a single integer t (1≤t≤104) — the number of test cases.

The description of each test case consists of four distinct integers a, b, c, d (0≤a,b,c,d≤104).

Output
For each test case, output a single integer — the number of participants in front of Timur.

Example

Input
4
2 3 4 1
10000 0 1 2
500 600 400 300
0 9999 10000 9998

Output
2
0
1
3
"""

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