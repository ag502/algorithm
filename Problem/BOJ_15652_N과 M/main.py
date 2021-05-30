from sys import stdin
from typing import List


def main():
    stdin = open("./input.txt", "r")

    n: int
    m: int
    n, m = list(map(int, stdin.readline().split()))

    def find_sequence(cur_num: int, sequence: List[int] = []):
        sequence.append(cur_num)

        if len(sequence) < m:
            for next_num in range(cur_num, n + 1):
                find_sequence(next_num, sequence)
        elif len(sequence) == m:
            print(' '.join(map(str, sequence)))
        sequence.pop()

    for start_num in range(1, n + 1):
        find_sequence(start_num)


if __name__ == '__main__':
    main()