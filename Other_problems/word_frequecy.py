
"""
Take a sentence as input and print how many times each word appears.

Example
Input:
apple banana apple mango banana apple

Output:
apple : 3
banana : 2
mango : 1
"""

all_words = input().split()
words_frequency = {}

for word in all_words:
    if word in words_frequency.keys():
        words_frequency[word] +=1
    else:
        words_frequency[word] = 1

for k , v in words_frequency.items():
    print(f"{k} : {v}")