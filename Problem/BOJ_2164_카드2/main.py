from sys import stdin
from collections import deque


def main():
    num_of_card = int(stdin.readline())
    card_queue = deque()

    for number in range(1, num_of_card + 1):
        card_queue.append(number)

    if len(card_queue) == 1:
        print(card_queue.popleft())
        return

    while True:
        card_queue.popleft()
        move_to_end = card_queue.popleft()

        if len(card_queue) == 0:
            print(move_to_end)
            return

        card_queue.append(move_to_end)


if __name__ == "__main__":
    main()
