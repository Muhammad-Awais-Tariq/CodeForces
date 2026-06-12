import sys
input = sys.stdin.readline

def solve():

    n , h = map(int, input().strip().split())
    heights = list(map(int, input().strip().split()))
    count = 0
    
    for height in heights:
        if height > h:
            count +=2
        else:
            count += 1
    
    print(count)
    


if __name__ == "__main__":
    solve()