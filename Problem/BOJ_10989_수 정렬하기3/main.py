from sys import stdin


def main():
    test_case = int(stdin.readline())
    number_array = [0] * 10001

    for _ in range(test_case):
        number_array[int(stdin.readline())] += 1

    for idx in range(len(number_array)):
        if number_array[idx] != 0:
            for _ in range(number_array[idx]):
                print(idx)


if __name__ == "__main__":
    main()