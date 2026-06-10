import sys
input = sys.stdin.readline

def solve():
    words = input().strip()
    lower_count = 0
    upper_count = 0

    for word in words:
        if word.islower():
            lower_count += 1
        else:
            upper_count += 1

    if upper_count > lower_count:
        print(words.upper())
    else:
        print(words.lower())

if __name__ == "__main__":
    solve()