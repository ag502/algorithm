from sys import stdin
from collections import *


def main():
    num_of_card = int(stdin.readline())
    card_counter = Counter()

    for _ in range(num_of_card):
        card = int(stdin.readline())
        card_counter[card] += 1

    card_counter = sorted(card_counter.items(), key=lambda x: (-x[1], x[0]))

    print(card_counter[0][0])


if __name__ == "__main__":
    main()
