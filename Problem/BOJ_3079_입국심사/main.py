from sys import stdin


def check_validation(total_time):
    count = 0
    for time in immigration:
        count += total_time // time

    if count >= m:
        return True
    return False


def binary_search():
    start = 1
    end = immigration[n - 1] * m

    while start <= end:
        mid = (start + end) // 2
        if check_validation(mid):
            end = mid - 1
        else:
            start = mid + 1
    return start


def main():
    stdin = open("./input.txt", "r")
    global n, m, immigration
    n, m = map(int, stdin.readline().split())
    immigration = []

    for _ in range(n):
        immigration.append(int(stdin.readline()))
    immigration.sort()

    print(binary_search())


if __name__ == '__main__':
    main()