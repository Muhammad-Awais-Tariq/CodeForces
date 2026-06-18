import sys
input = sys.stdin.readline

"""
You are given a binary array a of n elements, a binary array is an array consisting only of 0s and 1s.

A blank space is a segment of consecutive elements consisting of only 0s.

Your task is to find the length of the longest blank space.

Input
The first line contains a single integer t (1≤t≤1000) — the number of test cases.

The first line of each test case contains a single integer n (1≤n≤100) — the length of the array.

The second line of each test case contains n space-separated integers ai (0≤ai≤1) — the elements of the array.

Output
For each test case, output a single integer — the length of the longest blank space.

Example

Input
5
5
1 0 0 1 0
4
0 1 1 1
1
0
3
1 1 1
9
1 0 0 0 1 0 0 0 1

Output
2
1
1
0
3
"""
def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        longest = 0
        current = 0

        for num in arr:
            if num == 0:
                current += 1
                longest = max(longest, current)
            else:
                current = 0

        print(longest)

if __name__ == "__main__":
    solve()