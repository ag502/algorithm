from sys import stdin


def main():
    k, n = list(map(int, stdin.readline().split()))
    length_of_cables = [int(stdin.readline()) for _ in range(k)]

    start, end = 1, max(length_of_cables)

    while start <= end:
        mid = (start + end) // 2
        lines = 0

        for cable in length_of_cables:
            lines += cable // mid

        if lines >= n:
            start = mid + 1
        elif lines < n:
            end = mid - 1

    print(end)

if __name__ == "__main__":
    main()