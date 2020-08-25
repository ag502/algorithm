from sys import stdin


def main():
    x_pos = set()
    y_pos = set()

    for _ in range(3):
        X, Y = map(int, stdin.readline().split())
        if X in x_pos:
            x_pos.remove(X)
        else:
            x_pos.add(X)

        if Y in y_pos:
            y_pos.remove(Y)
        else:
            y_pos.add(Y)

    x_pos = list(x_pos)
    y_pos = list(y_pos)
    print(str(x_pos[0]) + " " + str(y_pos[0]))


if __name__ == "__main__":
    main()
