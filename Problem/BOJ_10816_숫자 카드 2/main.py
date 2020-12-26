from sys import stdin
from collections import Counter

MAX = 5 * (10 ** 5)


def main():
    stdin = open('input.txt', 'r')
    n = int(stdin.readline())
    cards = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())
    numbers = list(map(int, stdin.readline().split()))

    answer = [0] * MAX

    cards_list = Counter(cards)

    for idx, number in enumerate(numbers):
        if number in cards_list:
            answer[idx] = cards_list[number]

    print(' '.join(map(str, answer[:m])))


if __name__ == '__main__':
    main()