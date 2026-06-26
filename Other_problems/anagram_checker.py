
"""
Problem : Check if Two Strings are Anagrams

Two words are anagrams if they contain the same letters with the same frequencies, just in a different order.

Write a program that:

Takes two strings as input.
Prints "Anagram" if they are anagrams.
Otherwise, prints "Not Anagram".

Example 

Input
listen
silent

Output
Anagram
"""

word1 = input()
word2 = input()
word1_letter_dict = {}
word2_letter_dict = {}

if len(word1) != len(word2):
    print("Not Anagram")
else:
    for letter in word1:
        if letter in word1_letter_dict:
            word1_letter_dict[letter] += 1
        else:
            word1_letter_dict[letter] = 1
    
    for letter in word2:
        if letter in word2_letter_dict:
            word2_letter_dict[letter] += 1
        else:
            word2_letter_dict[letter] = 1    

    print("Anagram" if word1_letter_dict == word2_letter_dict else "Not Anagram")