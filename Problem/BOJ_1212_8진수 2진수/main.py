from sys import stdin


def main():
    stdin = open("./input.txt", "r")
    octal = "0o" + stdin.readline().rstrip()
    print(format(int(octal, 8), "b"))


if __name__ == '__main__':
    main()
