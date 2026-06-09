import sys
input = sys.stdin.readline

def solve():

    n = int(input())
    stones = input().strip()
    moves = 0

    for i in range(n):
        try:
            if stones[i] == stones[i+1]:
                moves +=1
        except IndexError:
            pass
    
    print(moves)
if __name__ == "__main__":
    solve()