import sys
input = sys.stdin.readline

def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        if arr[0] == arr[1]:
            common_value = arr[0]

            for i in range(n):
                if arr[i] != common_value:
                    print(i + 1)
                    break

        elif arr[0] == arr[2]:
            print(2)  

        else:
            print(1)  

if __name__ == "__main__":
    solve()