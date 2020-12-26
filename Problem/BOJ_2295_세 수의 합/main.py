from sys import stdin


def binary_search(array, start_idx, target):
    start = start_idx
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1


def main():
    stdin = open('input.txt', 'r')
    num_of_set = int(stdin.readline())

    number_set = [0] * num_of_set
    for idx in range(num_of_set):
        number_set[idx] = int(stdin.readline())

    number_set.sort()
    for target_idx in range(len(number_set) - 1, -1, -1):
        target_number = number_set[target_idx]
        for i in range(len(number_set)):
            for j in range(i, len(number_set)):
                if binary_search(number_set, j, target_number - number_set[i] - number_set[j]) != -1:
                    print(target_number)
                    return


if __name__ == '__main__':
    main()