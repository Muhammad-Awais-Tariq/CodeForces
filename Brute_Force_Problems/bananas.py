import sys
input = sys.stdin.readline

def solve():

    k , n , w = map(int, input().split())
    total_amount = 0
    for i in range(1 ,w+1):
        total_amount += i * k
    diff = total_amount - n
    if diff > 0 :
        print(total_amount - n) 
    else:
        print(0)

if __name__ == "__main__":
    solve()