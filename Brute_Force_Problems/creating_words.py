import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    for _ in range(n):
        s1 , s2 = map(list , input().split())
        s1[0] , s2[0] = s2[0] , s1[0]
        print(f"{"".join(s1)} {"".join(s2)}")

if __name__ == "__main__":
    solve()