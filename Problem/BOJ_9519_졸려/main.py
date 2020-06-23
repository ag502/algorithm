from sys import stdin
from collections import deque

def rotate(sequence):
    left = 0
    right = len(sequence) - 1
    rotated_sequence = [0] * len(sequence)

    current_index = 0
    while left <= right:
        if left == right:
            rotated_sequence[current_index] = sequence[left]
            break
        rotated_sequence[current_index] = sequence[left]
        current_index += 1
        rotated_sequence[current_index] = sequence[right]
        current_index += 1
        left += 1
        right -= 1
    return rotated_sequence

def main():
    n = int(stdin.readline())
    input_string = list(stdin.readline().rstrip())
    current_string_sequence = input_string

    cycle = 1
    while True:
        rotated_sequence = rotate(current_string_sequence)
        if input_string == rotated_sequence:
            break
        current_string_sequence = rotated_sequence
        cycle += 1

    current_string_sequence = input_string
    to_original_time = cycle - (n % cycle)
    for _ in range(0, to_original_time):
        current_string_sequence = rotate(current_string_sequence)

    print(''.join(current_string_sequence))


if __name__ == "__main__":
    main()
