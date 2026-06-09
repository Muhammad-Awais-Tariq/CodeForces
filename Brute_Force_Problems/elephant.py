import sys
input = sys.stdin.readline
import math

"""
An elephant decided to visit his friend. It turned out that the elephant's house is located at point 0 and his friend's house is located at point x(x>0) of the coordinate line. In one step the elephant can move 1, 2, 3, 4 or 5 positions forward. Determine, what is the minimum number of steps he need to make in order to get to his friend's house.

Input
The first line of the input contains an integer x (1≤x≤1000000) — The coordinate of the friend's house.

Output
Print the minimum number of steps that elephant needs to make to get from point 0 to point x.

Examples

Input
5

Output
1

Input
12

Output
3
"""

def solve():
    n = int(input())
    steps = math.ceil(n/5)
    print(steps)
    

if __name__ == "__main__":
    solve()