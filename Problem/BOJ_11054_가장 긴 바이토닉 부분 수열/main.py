from sys import stdin


def main():
    N = int(stdin.readline().rstrip())
    number_list = list(map(int, stdin.readline().split()))
    cache = [[1] * N for _ in range(2)]

    for i in range(1, len(number_list)):
        for j in range(0, i):
            if number_list[i] > number_list[j]:
                cache[0][i] = max(cache[0][i], cache[0][j] + 1)

    for i in range(len(number_list) - 2, -1, -1):
        for j in range(len(number_list) - 1, i, -1):
            if number_list[i] > number_list[j]:
                cache[1][i] = max(cache[1][i], cache[1][j] + 1)

    print(max(map(sum, zip(*cache))) - 1)


if __name__ == "__main__":
    main()
