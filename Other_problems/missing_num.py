n = int(input())
numbers = list(map(int , input().split()))
all_numbers_sum = sum([i for i in range(1,n+1)])
given_num_sum = sum(numbers)

missing = all_numbers_sum - given_num_sum

print(missing)