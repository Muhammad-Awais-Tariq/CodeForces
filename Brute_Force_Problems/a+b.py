import sys
input = sys.stdin.readline

"""
You are given an expression of the form a+b, where a and bare integers from 0 to 9. You have to evaluate it and print the result.

Input
The first line contains one integer t(1≤t≤100) — the number of test cases.

Each test case consists of one line containing an expression of the form a+b (0≤a,b≤9 , both a and b are integers). The integers are not separated from the +sign.

Output
For each test case, print one integer — the result of the expression.

Example

Input
4
4+2
0+0
3+7
8+9

Output
6
0
10
17
"""

def solve():
    n = int(input())
    for _ in range(n):
        expression = input().strip()
        print(eval(expression))

if __name__ == "__main__":
    solve()