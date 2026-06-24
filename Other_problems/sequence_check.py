
total_num = int(input())
numbers = list(map(int , input().split()))
consecutive = True
for i in range(total_num-1):
    if numbers[i+1] - numbers[i] != 1:
        consecutive = False
        break

print("YES" if consecutive else "NO")