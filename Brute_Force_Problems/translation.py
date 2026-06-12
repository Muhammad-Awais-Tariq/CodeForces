import sys
input = sys.stdin.readline

def solve():
    word1 = input().strip()
    word2 = input().strip()

    if word2[::-1] == word1:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()