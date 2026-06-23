string = input()
all_chars = list(set(string))
all_chars.sort()
max_count = 0
max_char = ""
for char in all_chars:
    count = string.count(char)
    if count > max_count:
        max_count = count
        max_char = char
    elif count == max_count:
        continue

print(max_char)