import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    room_avaliable = 0

    for _ in range(n):
        p , q = map(int , input().split())
        if (q - p) >= 2:
            room_avaliable += 1
    
    print(room_avaliable)

if __name__ == "__main__":
    solve()