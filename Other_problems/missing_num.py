
"""
Find the Missing Number

You are given n-1 distinct numbers from 1 to n. One number is missing. Find it.

Example
Input:
5
1 2 4 5

Output:
3
"""

n = int(input())
numbers = list(map(int , input().split()))
all_numbers_sum = sum([i for i in range(1,n+1)])
given_num_sum = sum(numbers)

missing = all_numbers_sum - given_num_sum

print(missing)