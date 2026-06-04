import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    total_count = 0
    for i in range(n):
        word = input()
        if word.count("1") >= 2:
            total_count +=1
    
    print(total_count)

if __name__ == "__main__":
    solve()