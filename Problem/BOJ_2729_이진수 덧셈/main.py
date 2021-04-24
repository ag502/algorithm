from sys import stdin


def main():
    stdin = open("./input.txt", "r")

    test_case = int(stdin.readline())

    for _ in range(test_case):
        bin_digit1, bin_digit2 = stdin.readline().rstrip().split()
        print(bin((int(bin_digit1, 2) + int(bin_digit2, 2)))[2:])


if __name__ == '__main__':
    main()