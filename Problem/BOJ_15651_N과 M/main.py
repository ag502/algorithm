from sys import stdin
from typing import List


def find_sequence(cur_num: int, sequence: List[int], m: int, n: int) -> None:
    sequence.append(cur_num)

    if len(sequence) < m:
        for next_num in range(1, n + 1):
            find_sequence(next_num, sequence, m, n)
    elif len(sequence) == m:
        print(' '.join(map(str, sequence)))
    sequence.pop()


def main() -> None:
    stdin = open("input.txt", "r")
    n: int
    m: int
    n, m = list(map(int, stdin.readline().split()))
    sequence: List[int] = []

    for start_num in range(1, n + 1):
        find_sequence(start_num, sequence, m, n)


if __name__ == '__main__':
    main()