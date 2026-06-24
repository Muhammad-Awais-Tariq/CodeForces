total_num = input().split()
numbers = list(map(int , input().split()))
unique_num = list(set(numbers))
unique_num.sort()
max_number_count = 0
max_number = -1

for num in unique_num:
    count = numbers.count(num)
    if count > max_number_count:
        max_number_count = count
        max_number = num

print(max_number)