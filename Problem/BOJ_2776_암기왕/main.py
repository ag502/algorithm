from sys import stdin


def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


def main():
    stdin = open('./input.txt', 'r')
    test_case = int(stdin.readline())

    for _ in range(test_case):
        num_of_number_in_note_1 = int(stdin.readline())
        note_1 = list(map(int, stdin.readline().split()))

        num_of_number_in_note_2 = int(stdin.readline())
        note_2 = list(map(int, stdin.readline().split()))

        note_1.sort()
        for num in note_2:
            print(binary_search(note_1, num))


if __name__ == '__main__':
    main()