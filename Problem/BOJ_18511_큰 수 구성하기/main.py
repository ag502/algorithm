from sys import stdin
from collections import deque

stdin = open("./input.txt", "r")
N, num_of_elements = map(int, stdin.readline().split())
numbers = list(map(int, stdin.readline().split()))

answer = 0


def dfs(cur_idx, temp):
    global answer
    temp.append(numbers[cur_idx])

    if len(temp) < len(str(N)):
        for next_idx in range(num_of_elements):
            dfs(next_idx, temp)

    number = int(''.join(map(str, temp)))
    if N >= number > answer:
        answer = number
    temp.pop()


def main():
    for idx in range(num_of_elements):
        dfs(idx, deque())

    print(answer)


if __name__ == '__main__':
    main()