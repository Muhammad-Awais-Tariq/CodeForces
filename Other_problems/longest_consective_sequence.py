

numbers = list(map(int, input().split()))

if len(numbers) == 0:
    print(0)
else:
    current_sequence_length = 1
    max_sequence_length = 1

    for i in range(len(numbers) - 1):
        if numbers[i] + 1 == numbers[i + 1]:
            current_sequence_length += 1
        else:
            if current_sequence_length > max_sequence_length:
                max_sequence_length = current_sequence_length
            current_sequence_length = 1

    if current_sequence_length > max_sequence_length:
        max_sequence_length = current_sequence_length

    print(max_sequence_length)