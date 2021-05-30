from sys import stdin
from typing import List, Any


def main() -> None:
    stdin = open("./input.txt", "r")
    n: int
    m: int
    n, m = list(map(int, stdin.readline().split()))
    visited: List[bool] = [False] * (n + 1)

    def find_sequence(cur_num: int, sequence: List[int] = []) -> None:
        sequence.append(cur_num)
        visited[cur_num] = True

        if len(sequence) < m:
            for next_num in range(1, n + 1):
                if not visited[next_num]:
                    find_sequence(next_num, sequence)
        elif len(sequence) == m:
            print(' '.join(map(str, sequence)))
        sequence.pop()
        visited[cur_num] = False

    for start_num in range(1, n + 1):
        find_sequence(start_num)


if __name__ == "__main__":
    main()