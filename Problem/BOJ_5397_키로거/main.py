from sys import stdin
from collections import deque


def key_logger(string):
    left_queue = deque()
    right_queue = deque()

    for char in string:
        if char == ">":
            if right_queue:
                left_queue.append(right_queue.popleft())
            else:
                continue
        elif char == "<":
            if left_queue:
                right_queue.appendleft(left_queue.pop())
            else:
                continue
        elif char == "-":
            if left_queue:
                left_queue.pop()
            else:
                continue
        else:
            left_queue.append(char)

    return ''.join(left_queue + right_queue)


def main():
    stdin = open("./input.txt", "r")
    test_case = int(stdin.readline())

    for _ in range(test_case):
        string = stdin.readline().rstrip()
        print(key_logger(string))


if __name__ == '__main__':
    main()