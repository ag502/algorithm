from sys import stdin


def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
    return 0


def main():
    n = int(stdin.readline())
    num_list = sorted(list(map(int, stdin.readline().split())))
    m = int(stdin.readline())
    find_num_list = list(map(int, stdin.readline().split()))

    for number in find_num_list:
        if binary_search(num_list, number) == 1:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    main()
