from sys import stdin
from typing import List, Tuple


def get_sum(num_1: int, num_2: int) -> int:
    return num_1 + num_2


def main() -> int:
    stdin = open("./input.txt", "r")
    num_1: int
    num_2: int
    num_1, num_2 = list(map(int, stdin.readline().split(" ")))
    result: int = get_sum(num_1, num_2)
    print(result)
    return result


if __name__ == '__main__':
    main()