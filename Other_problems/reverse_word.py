
"""
Problem: Reverse Each Word

Write a program that:

Takes a sentence as input.
Reverses each word individually while keeping the word order the same.

Example
Input
hello python world

Output
olleh nohtyp dlrow
"""

words = input().split()
revers_words = []

for word in words:
    revers_words.append(word[::-1])

print(revers_words)