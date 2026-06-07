import sys
input = sys.stdin.readline

def solve():
    j = input().lower().strip()
    l = input().lower().strip()
    output = 0

    for i in range(len(j)):
        if ord(j[i].lower()) >  ord(l[i].lower()):
            output = 1
            break
        elif ord(j[i].lower()) <  ord(l[i].lower()):
            output = -1
            break

    print(output)


if __name__ == "__main__":
    solve()

