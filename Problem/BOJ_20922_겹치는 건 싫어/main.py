from sys import stdin
from collections import deque

stdin = open("./input.txt", "r")
array_len, limit = map(int, stdin.readline().split())
array = list(map(int, stdin.readline().split()))

count_array = [0] * 100001


def main():
    answer = 0
    start, end = 0, 0
    cur_left = array[start]
    count_array[cur_left] += 1

    if array_len == 1:
        print(1)
        return

    while True:
        end += 1
        if end >= array_len:
            break

        cur_right = array[end]
        count_array[cur_right] += 1

        while count_array[cur_right] > limit:
            count_array[cur_left] -= 1
            start += 1
            cur_left = array[start]
        answer = max(answer, abs(start - end) + 1)

    print(answer)


if __name__ == '__main__':
    main()
