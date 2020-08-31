from sys import stdin


def main():
    N = int(stdin.readline().rstrip())
    stair_score = [0] * 301
    cache = [[0, 0] for _ in range(301)]

    for i in range(1, N + 1):
        score = int(stdin.readline().rstrip())
        stair_score[i] = score

    cache[1][0] = stair_score[1]
    cache[2][0] = stair_score[1] + stair_score[2]
    cache[2][1] = stair_score[2]

    for stair in range(3, N + 1):
        cache[stair][0] = cache[stair - 1][1] + stair_score[stair]
        cache[stair][1] = max(cache[stair - 2][0],
                              cache[stair - 2][1]) + stair_score[stair]

    print(max(cache[N][0], cache[N][1]))


if __name__ == "__main__":
    main()
