
"""
Longest Consecutive Increasing Sequence

Given a list of integers, find the length of the longest consecutive increasing sequence.

A sequence is consecutive increasing if each next element is exactly 1 greater than the previous one.

Input
8
1 2 3 8 9 10 11 5
Output
4

Explanation:

1 2 3 → length = 3
8 9 10 11 → length = 4

So the answer is 4.
"""

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