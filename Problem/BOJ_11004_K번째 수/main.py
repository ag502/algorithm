from sys import stdin


def main():
    n, k = list(map(int, stdin.readline().split()))

    number_array = list(map(int, stdin.readline().split()))
    number_array.sort()

    print(number_array[k - 1])


if __name__ == "__main__":
    main()