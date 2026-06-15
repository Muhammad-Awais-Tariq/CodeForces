import sys
input = sys.stdin.readline

"""
There is a string s of length 3, consisting of uppercase and lowercase English letters. Check if it is equal to "YES" (without quotes), where each letter can be in any case. For example, "yES", "Yes", "yes" are all allowable.

Input
The first line of the input contains an integer t(1≤t≤103) — the number of testcases.

The description of each test consists of one line containing one string s consisting of three characters. Each character of s is either an uppercase or lowercase English letter.

Output
For each test case, output "YES" (without quotes) if s satisfies the condition, and "NO" (without quotes) otherwise.

You can output "YES" and "NO" in any case (for example, strings "yES", "yes" and "Yes" will be recognized as a positive response).

Example

Input
10
YES
yES
yes
Yes
YeS
Noo
orZ
yEz
Yas
XES

Output
YES
YES
YES
YES
YES
NO
NO
NO
NO
NO

Note

The first five test cases contain the strings "YES", "yES", "yes", "Yes", "YeS". All of these are equal to "YES", where each character is either uppercase or lowercase.

"""

def solve():
    n = int(input())

    for _ in range(n):
        print("YES" if input().lower().strip() == "yes" else "NO")

if __name__ == "__main__":
    solve()