from sys import stdin
from math import pi


def main():
    R = int(input())

    print('%.6f' % (pi * (R ** 2)))
    print('%.6f' % ((R ** 2) * 2))


if __name__ == "__main__":
    main()
