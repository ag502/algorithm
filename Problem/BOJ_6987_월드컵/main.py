from sys import stdin
from itertools import combinations


def main():
    stdin = open("./input.txt", "r")

    score_boards = []
    for _ in range(4):
        score_board = []
        score = list(map(int, stdin.readline().split()))
        for idx in range(0, len(score) - 2, 3):
            score_board.append([score[idx], score[idx + 1], score[idx + 2]])
        score_boards.append(score_board)

    print(score_boards)


if __name__ == '__main__':
    main()
