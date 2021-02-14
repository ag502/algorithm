from sys import stdin

origin_numbers = None


def binary_search(target_number, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if target_number == origin_numbers[mid]:
        return 1
    elif target_number > origin_numbers[mid]:
        return binary_search(target_number, mid + 1, end)
    else:
        return binary_search(target_number, start, mid - 1)


def main():
    global origin_numbers
    stdin = open("./input.txt")

    num_of_numbers = int(stdin.readline())
    origin_numbers = list(map(int, stdin.readline().split()))
    origin_numbers.sort()

    num_of_target_nums = int(stdin.readline())
    target_numbers = list(map(int, stdin.readline().split()))

    for target_num in target_numbers:
        print(binary_search(target_num, 0, len(origin_numbers) - 1))


if __name__ == '__main__':
    main()