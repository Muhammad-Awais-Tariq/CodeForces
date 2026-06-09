import sys
input = sys.stdin.readline

def solve():
    a, b = map(int, input().strip().split())
    i = 0
   
    while (True):
        a = a *3
        b = b * 2
        i += 1
        if a > b:
            break
    
    print(i)
        
if __name__ == "__main__":
    solve()