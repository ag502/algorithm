from sys import stdin


def get_sum(num_1: int, num_2: int) -> int:
    return num_1 + num_2


def main() -> None:
    stdin = open("./input.txt", "r")
    num_1, num_2 = list(map(int, stdin.readline().split(" ")))
    print(get_sum(num_1, num_2))


if __name__ == '__main__':
    main()