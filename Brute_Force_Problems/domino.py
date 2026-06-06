import sys
input = sys.stdin.readline

def solve():

    m, n = map(int, input().split())
    board_size = m * n

    print(board_size//2) # integer devision in python gives the floor value

if __name__ == "__main__":
    solve()