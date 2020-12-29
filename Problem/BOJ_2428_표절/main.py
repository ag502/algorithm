from sys import stdin


def upper_bound(array, start_idx, target):
    start = start_idx
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] <= target:
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
    for idx in range(len(sizes) - 1):
        print(upper_bound(sizes, idx + 1, sizes[idx] * 0.9))
        num_of_check_files += upper_bound(sizes, idx + 1, sizes[idx] * 0.9)

    print(num_of_check_files)


if __name__ == '__main__':
    main()