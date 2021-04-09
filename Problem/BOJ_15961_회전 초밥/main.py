from sys import stdin
from collections import deque

stdin = open("./input.txt", "r")

num_of_plates, num_of_sushi, k, c = map(int, stdin.readline().split())
belt = deque()

for _ in range(num_of_plates):
    belt.append(int(stdin.readline()))

for idx in range(k - 1):
    belt.append(belt[idx])


def main():
    cur_sushi = {c: 1}
    start = 0
    end = k - 1

    for idx in range(k):
        if belt[idx] in cur_sushi:
            cur_sushi[belt[idx]] += 1
        else:
            cur_sushi[belt[idx]] = 1

    answer = len(cur_sushi)

    while True:
        if (cur_sushi[belt[start]] - 1) == 0:
            del cur_sushi[belt[start]]
        else:
            cur_sushi[belt[start]] -= 1
        start += 1

        if end >= len(belt) - 1:
            break
        end += 1
        if belt[end] in cur_sushi:
            cur_sushi[belt[end]] += 1
        else:
            cur_sushi[belt[end]] = 1

        answer = max(answer, len(cur_sushi))
        if answer == k + 1:
            break

    print(answer)


if __name__ == '__main__':
    main()