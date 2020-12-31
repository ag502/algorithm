from sys import stdin
from math import floor


def main():
    stdin = open('./input.txt', 'r')
    total_rounds, win_rounds = map(int, stdin.readline().split())
    cur_win_rate = floor((win_rounds / total_rounds) * 100)

    if cur_win_rate == 100:
        print(-1)
        return

    additional_games = 0
    while True:
        additional_games += 1
        new_win_rate = floor(((win_rounds + additional_games) / (total_rounds + additional_games)) * 100)
        if cur_win_rate != new_win_rate:
            print(additional_games)
            break


if __name__ == '__main__':
    main()