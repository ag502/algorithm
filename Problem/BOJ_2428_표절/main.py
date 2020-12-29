from sys import stdin


def lower_bound(array, start_idx, end_idx, target):
    start = start_idx
    end = end_idx

    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


def main():
    stdin = open('./input.txt', 'r')
    num_of_solutions = int(stdin.readline())
    sizes = list(map(int, stdin.readline().split()))

    sizes.sort()

    num_of_check_files = 0
    for idx in range(len(sizes) - 1, 0, -1):
        num_of_check_files += idx - lower_bound(sizes, 0, idx - 1, sizes[idx] * 0.9)

    print(num_of_check_files)


if __name__ == '__main__':
    main()