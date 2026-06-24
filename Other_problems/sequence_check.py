
"""
Given an array of integers, determine whether every adjacent pair differs by exactly 1.

Input
5
3 4 5 6 7

Output
YES

Input
5
3 4 6 7 8

Output
NO
"""

total_num = int(input())
numbers = list(map(int , input().split()))
consecutive = True
for i in range(total_num-1):
    if numbers[i+1] - numbers[i] != 1:
        consecutive = False
        break

print("YES" if consecutive else "NO")