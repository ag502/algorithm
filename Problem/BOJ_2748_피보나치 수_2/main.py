from sys import stdin


def main():
    cache = [0] * 91
    cache[0] = 0
    cache[1] = 1

    N = int(stdin.readline().rstrip())

    for i in range(2, N + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    print(cache[N])


if __name__ == "__main__":
    main()
