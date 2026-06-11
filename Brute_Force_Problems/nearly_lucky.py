import sys
input = sys.stdin.readline

def solve():
    number = input().strip()
    lucky_count = 0

    for n in number:
        if n == "7" or n == "4":
            lucky_count += 1
    
    if lucky_count == 7 or lucky_count == 4:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()