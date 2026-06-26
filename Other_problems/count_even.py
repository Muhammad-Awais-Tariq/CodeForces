

size = int(input())
numbers = list(map(int , input().split()))
count = 0

for num in numbers :
    if num % 2 == 0:
        count +=1

print(count)