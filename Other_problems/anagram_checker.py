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