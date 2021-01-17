from sys import stdin
from collections import deque


def string_process(string, last_char):
    processed_string = ''
    if last_char == 'A':
        processed_string = string[:len(string) - 1]
    elif last_char == 'B':
        processed_string = ''.join(list(reversed(string[:len(string) - 1])))
    return processed_string


def main():
    stdin = open('./input.txt', 'r')
    start_string = stdin.readline().strip()
    target_string = stdin.readline().strip()

    while len(start_string) != len(target_string):
        target_string = string_process(target_string, target_string[len(target_string) - 1])

    print(1 if start_string == target_string else 0)


if __name__ == '__main__':
    main()