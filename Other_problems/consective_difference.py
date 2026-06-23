n = int(input())
array = list(map(int , input().split()))
i = 0
successful = True

while i < n-1:
    diff = array[i+1] - array[i]
    if diff == 1:
        i = i+1
    else:
        successful = False
        break
if successful:
    print("Yes")
else:
    print("No")

