
"""
Given n integers, find the number that appears most frequently.

If multiple numbers have the same highest frequency, output the smallest one.

Input
8
1 2 2 3 3 3 4 4

Output
3

Input
6
1 1 2 2 3 3

Output
1
"""

total_num = input().split()
numbers = list(map(int , input().split()))
unique_num = list(set(numbers))
unique_num.sort()
max_number_count = 0
max_number = -1

for num in unique_num:
    count = numbers.count(num)
    if count > max_number_count:
        max_number_count = count
        max_number = num

print(max_number)