import sys
input = sys.stdin.readline

"""
Matthew is given two strings a and b, both of length 3. He thinks it's particularly funny to create two new words by swapping the first character of a with the first character of b. He wants you to output a and b after the swap.

Note that the new words may not necessarily be different.

Input
The first line contains t (1≤t≤100)  — the number of test cases.

The first and only line of each test case contains two space-separated strings, a and b, both of length 3. The strings only contain lowercase Latin letters.

Output
For each test case, after the swap, output a and b, separated by a space.

Example

Input
6
bit set
cat dog
hot dog
uwu owo
cat cat
zzz zzz

Output
sit bet
dat cog
dot hog
owu uwo
cat cat
zzz zzz
"""

def solve():
    n = int(input())
    for _ in range(n):
        s1 , s2 = map(list , input().split())
        s1[0] , s2[0] = s2[0] , s1[0]
        print(f"{"".join(s1)} {"".join(s2)}")

if __name__ == "__main__":
    solve()