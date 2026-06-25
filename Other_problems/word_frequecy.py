all_words = input().split()
words_frequency = {}

for word in all_words:
    if word in words_frequency.keys():
        words_frequency[word] +=1
    else:
        words_frequency[word] = 1

for k , v in words_frequency.items():
    print(f"{k} : {v}")