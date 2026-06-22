import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    ans = 0

    for i in range(10):
        s = input().strip()

        for j in range(10):
            if s[j] == 'X':
                ans += min(i + 1, j + 1, 10 - i, 10 - j)

    print(ans)