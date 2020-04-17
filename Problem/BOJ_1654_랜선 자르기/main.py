from sys import stdin


def main():
    n, k = list(map(int, stdin.readline().split()))

    length_of_cables = []
    for _ in range(0, n):
        cable = int(stdin.readline())
        length_of_cables.append(cable)

    max_length = sum(length_of_cables) // k

    for length in range(max_length, 0, -1):
        num_of_cable = list(map(lambda x: x // length, length_of_cables))

        if sum(num_of_cable) == k:
            print(length)
            break


if __name__ == "__main__":
    main()
