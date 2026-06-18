import sys
input = sys.stdin.readline

"""
Codeforces separates its users into 4 divisions by their rating:

For Division 1: 1900≤rating
For Division 2: 1600≤rating≤1899
For Division 3: 1400≤rating≤1599
For Division 4: rating≤1399

Given a rating , print in which division the rating belongs.

Input
The first line of the input contains an integer t (1≤t≤104) — the number of testcases.

The description of each test case consists of one line containing one integer rating (-5000≤rating≤5000).

Output
For each test case, output a single line containing the correct division in the format "Division X", where X is an integer between 1 and 4 representing the division for the corresponding rating.

Example

Input
7
-789
1299
1300
1399
1400
1679
2300

Output
Division 4
Division 4
Division 4
Division 4
Division 3
Division 2
Division 1
"""

def solve():
    n = int(input())

    for _ in range(n):
        value = int(input())

        if value >= 1900:
            print("Division 1")
        elif 1899 >= value >= 1600:
            print("Division 2")
        elif 1599 >= value >= 1400:
            print("Division 3")
        else:
            print("Division 4")

if __name__ == "__main__":
    solve()