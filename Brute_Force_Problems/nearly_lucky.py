import sys
input = sys.stdin.readline

"""
Petya loves lucky numbers. We all know that lucky numbers are the positive integers whose decimal representations contain only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Unfortunately, not all numbers are lucky. Petya calls a number nearly lucky if the number of lucky digits in it is a lucky number. He wonders whether number n is a nearly lucky number.

Input
The only line contains an integer n (1≤n≤1018).

Output
Print on the single line "YES" if n is a nearly lucky number. Otherwise, print "NO" (without the quotes).

Examples

Input
40047

Output
NO

Input
7747774

Output
YES

Input
1000000000000000000

Output
NO

Note

In the first sample there are 3 lucky digits (first one and last two), so the answer is "NO".

In the second sample there are 7 lucky digits, 7 is lucky number, so the answer is "YES".

In the third sample there are no lucky digits, so the answer is "NO".


"""

def solve():
    number = input().strip()
    lucky_count = 0

    for n in number:
        if n == "7" or n == "4":
            lucky_count += 1
    
    if lucky_count == 7 or lucky_count == 4:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()