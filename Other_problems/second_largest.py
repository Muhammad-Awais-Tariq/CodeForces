
"""
Task:
Given n integers, find the second largest distinct number.

Input
5
10 20 30 40 50

Output
40
"""

numbers = list(set(map(int , input().split())))
numbers.sort(reverse=True)
print(numbers[1])