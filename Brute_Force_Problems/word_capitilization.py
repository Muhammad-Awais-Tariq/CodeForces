import sys
input = sys.stdin.readline

"""
Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

Note, that during capitalization all the letters except the first one remains unchanged.

Input
A single line contains a non-empty word. This word consists of lowercase and uppercase English letters. The length of the word will not exceed 103.

Output
Output the given word after capitalization.

Examples

Input
ApPLe

Output
ApPLe

Input
konjac

Output
Konjac
"""

def solve():
    word = list(input().strip())
    word[0]= word[0].upper()
    print("".join(word))

if __name__ == "__main__":
    solve()

