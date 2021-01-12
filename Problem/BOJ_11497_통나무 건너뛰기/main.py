from sys import stdin
from heapq import heapify, heappop


def main():
    stdin = open('./input.txt', 'r')

    test_case = int(stdin.readline())
    for _ in range(test_case):
        num_of_logs = int(stdin.readline())
        logs = list(map(int, stdin.readline().split()))
        heapify(logs)

        sorted_logs = [0] * len(logs)

        length = len(logs)
        for idx in range(length // 2):
            left = heappop(logs)
            right = heappop(logs)

            sorted_logs[idx] = left
            sorted_logs[length - 1 - idx] = right

        if len(logs) != 0:
            sorted_logs[length // 2] = heappop(logs)

        level = abs(sorted_logs[0] - sorted_logs[len(sorted_logs) - 1])
        for idx in range(len(sorted_logs) - 1):
            level = max(level, abs(sorted_logs[idx] - sorted_logs[idx + 1]))

        print(level)


if __name__ == '__main__':
    main()