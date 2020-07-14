from sys import stdin


def z_sum(grasses):
    return sum(grasses)


def n_grow(x, h, grasses):
    for idx, grass in enumerate(grasses):
        if grass + x <= h:
            grasses[idx] = grass + x
        else:
            grasses[idx] = h


def l_cut(x, grasses):
    for i in range(x):
        grasses[i] = 0


def d_cut(x, grasses):
    for i in range(len(grasses) - 1, len(grasses) - 1 - x, -1):
        grasses[i] = 0


def s_cut(x, grasses):
    for idx, grass in enumerate(grasses):
        if grass >= x:
            grasses[idx] = x


def main():
    n, h, m = map(int, stdin.readline().split())
    grasses = [0] * n

    for _ in range(m):
        query = stdin.readline().split()

        if query[0] == 'Z':
            print(z_sum(grasses))
        else:
            x = int(query[1])
            if query[0] == 'N':
                n_grow(x, h, grasses)
            elif query[0] == 'L':
                l_cut(x, grasses)
            elif query[0] == 'D':
                d_cut(x, grasses)
            elif query[0] == 'S':
                s_cut(x, grasses)


if __name__ == "__main__":
    main()
