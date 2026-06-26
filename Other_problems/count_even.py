
"""
Problem: Count Even Numbers

Write a program that:

Takes an integer n.
Takes n integers as input.
Prints how many of them are even.

"""
size = int(input())
numbers = list(map(int , input().split()))
count = 0

for num in numbers :
    if num % 2 == 0:
        count +=1

print(count)