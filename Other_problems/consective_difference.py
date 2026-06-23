
"""
Given a list of integers, determine whether the difference between every pair of consecutive elements is exactly 1.

Print "YES" if true, otherwise print "NO".

Input
First line: integer n
Second line: n space-separated integers
Output

Print YES or NO.

Example 
Input

5
3 4 5 6 7
Output

YES
"""

n = int(input())
array = list(map(int , input().split()))
i = 0
successful = True

while i < n-1:
    diff = array[i+1] - array[i]
    if diff == 1:
        i = i+1
    else:
        successful = False
        break
if successful:
    print("Yes")
else:
    print("No")

