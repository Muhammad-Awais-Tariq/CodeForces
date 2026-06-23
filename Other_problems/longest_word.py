sentence = input().split()
max_len = 0
max_word = ""
for word in sentence:
    if len(word) > max_len:
        max_len = len(word)
        max_word = word

print(max_word)
