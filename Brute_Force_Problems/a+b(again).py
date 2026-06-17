import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    for _ in range(n):
        entered_num = input().strip()
        sum_of_nums = int(entered_num[0]) + int(entered_num[1])
        print(sum_of_nums)


if __name__ == "__main__":
    solve()