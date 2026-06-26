words = input().split()
revers_words = []

for word in words:
    revers_words.append(word[::-1])

print(revers_words)