from sys import stdin


def get_count(target_number):
    count = 0
    for row in range(1, n + 1):
        count += min(target_number // row, n)
    return count


def binary_search():
    start = 1
    end = n * n

    while start <= end:
        mid = (start + end) // 2
        number_count = get_count(mid)
        if number_count < k:
            start = mid + 1
        else:
            end = mid - 1
    return start


def main():
    stdin = open("./input.txt", "r")
    global n, k
    n = int(stdin.readline())
    k = int(stdin.readline())

    print(binary_search())


if __name__ == '__main__':
    main()