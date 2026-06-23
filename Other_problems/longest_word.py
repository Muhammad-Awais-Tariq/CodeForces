
"""
Given a sentence containing words separated by spaces, find the longest word.

If multiple words have the same maximum length, print the first one.

Input

A single line containing a sentence.

Output

Print the longest word.

Example 

Input
python is awesome

Output
awesome
"""

sentence = input().split()
max_len = 0
max_word = ""
for word in sentence:
    if len(word) > max_len:
        max_len = len(word)
        max_word = word

print(max_word)
