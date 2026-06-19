import sys
input = sys.stdin.readline

"""
Suneet has three digits a, b, and c.

Since math isn't his strongest point, he asks you to determine if you can choose any two digits to make a sum greater or equal to 10.

Output "YES" if there is such a pair, and "NO" otherwise.

Input
The first line contains a single integer t (1≤t≤1000) — the number of test cases.

The only line of each test case contains three digits a, b, c (0≤a,b,c≤9).

Output
For each test case, output "YES" if such a pair exists, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

Example

Input
5
8 1 2
4 4 5
9 9 9
0 0 0
8 5 3

Output
YES
NO
YES
NO
YES

"""

def solve():
    n = int(input())

    for _ in range(n):
        a, b , c = map(int, input().split())
        print("YES"  if a + b >= 10 or a + c >= 10 or b + c >= 10 else "No")


if __name__ == "__main__":
    solve()