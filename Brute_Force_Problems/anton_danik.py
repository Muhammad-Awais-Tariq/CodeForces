import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    games_string = input().strip()
    a_points = 0
    d_points = 0

    for i in range(n):
        if games_string[i] == "A":
            a_points += 1
        else:
            d_points += 1  
    
    if a_points > d_points:
        print("Anton")
    elif d_points > a_points:
        print("Danik")
    else:
        print("Friendship")

if __name__ == "__main__":
    solve()