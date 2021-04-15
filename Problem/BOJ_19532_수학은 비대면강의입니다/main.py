from sys import stdin


def main():
    stdin = open("./input.txt", "r")
    a, b, c, d, e, f = map(int, stdin.readline().split())

    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if (a * x + b * y) == c and (d * x + e * y) == f:
                print(str(x) + " " + str(y))
                return


if __name__ == '__main__':
    main()