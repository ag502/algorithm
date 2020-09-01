from sys import stdin


def main():
    row, col = map(int, stdin.readline().split())
    square = []
    for _ in range(row):
        square.append(list(map(int, list(stdin.readline().rstrip()))))
    # print(square)

    max_size = 1
    # max_value = 0
    for i in range(row):
        for j in range(col):
            for length in range(1, len(square[i]) - j):
                if i + length >= row:
                    break
                else:
                    print(square[i][j],
                          square[i][j + length],
                          square[i + length][j],
                          square[i + length][j + length],
                          (length + 1) ** 2)
                    if square[i][j] == square[i][j + length] \
                            and square[i][j] == square[i + length][j] \
                            and square[i][j] == square[i + length][j + length]:
                        max_size = (
                            length + 1) ** 2 if max_size < (
                            length + 1) ** 2 else max_size
    print(max_size)


if __name__ == "__main__":
    main()
