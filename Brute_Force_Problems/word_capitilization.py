import sys
input = sys.stdin.readline

def solve():
    word = list(input().strip())
    word[0]= word[0].upper()
    print("".join(word))

if __name__ == "__main__":
    solve()

