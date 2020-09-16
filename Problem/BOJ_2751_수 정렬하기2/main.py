from sys import stdin

def merge(left_list, right_list):
    new_list = []
    left_ptr = 0
    right_ptr = 0

    while left_ptr < len(left_list) and right_ptr < len(right_list):
        if left_list[left_ptr] < right_list[right_ptr]:
            new_list.append(left_list[left_ptr])
            left_ptr += 1
        elif left_list[left_ptr] >= right_list[right_ptr]:
            new_list.append(right_list[right_ptr])
            right_ptr += 1

    if left_ptr >= len(left_list):
        new_list += right_list[right_ptr:]
    elif right_ptr >= len(right_list):
        new_list += left_list[left_ptr:]

    return new_list

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    return merge(
        merge_sort(input_list[:len(input_list) // 2]),
        merge_sort(input_list[len(input_list) // 2:])
    )

def main():
    N = int(stdin.readline())
    numbers = []

    for _ in range(N):
        numbers.append(int(stdin.readline()))

    answer = merge_sort(numbers)

    for number in answer:
        print(number)

if __name__ == '__main__':
    main()

