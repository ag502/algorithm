from sys import stdin


def main():
    triangle = []
    N = int(stdin.readline().rstrip())

    for _ in range(N):
        triangle.append(list(map(int, stdin.readline().split())))

    cache = [[0] * N for _ in range(N)]
    cache[0][0] = triangle[0][0]

    for row in range(0, len(triangle) - 1):
        for col in range(len(triangle[row])):
            cache[row + 1][col] = max(cache[row + 1][col],
                                      cache[row][col] + triangle[row + 1][col])
            cache[row + 1][col + 1] = max(cache[row + 1][col + 1],
                                          cache[row][col] + triangle[row + 1][col + 1])

    print(max(cache[N - 1]))


if __name__ == "__main__":
    main()
