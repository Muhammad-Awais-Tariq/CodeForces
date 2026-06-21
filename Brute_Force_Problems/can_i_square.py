import sys
input = sys.stdin.readline

"""
Calin has n buckets, the i-th of which contains ai wooden squares of side length 1.

Can Calin build a square using all the given squares?

Input
The first line contains a single integer t (1≤t≤104) — the number of test cases.

The first line of each test case contains a single integer n (1≤n≤2⋅105) — the number of buckets.

The second line of each test case contains n integers a1,…,an (1≤ai≤109) — the number of squares in each bucket.

The sum of n over all test cases does not exceed 2⋅105.

Output
For each test case, output "YES" if Calin can build a square using all of the given 1x1 squares, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

Example

Input
5
1
9
2
14 2
7
1 2 3 4 5 6 7
6
1 3 5 7 9 11
4
2 2 2 2

Output
YES
YES
NO
YES
NO
"""

def solve():
    total_iteration = int(input())
    for _ in range(total_iteration):
        total_square = int(input())
        sum_squares = sum(list(map(int, input().split())))
        square_root = sum_squares ** 0.5
        print("YES" if (sum_squares % square_root) == 0.0 else "NO")

if __name__ == "__main__":
    solve()