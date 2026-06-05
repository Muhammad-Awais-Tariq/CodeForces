import sys
input = sys.stdin.readline

def solve():
    n , k = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0

    for element in arr:
        if element >= arr[k-1] and element > 0:
            count +=1
    
    print(count)

if __name__ == "__main__":
    solve()