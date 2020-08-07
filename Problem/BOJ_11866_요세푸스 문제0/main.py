from sys import stdin
from collections import deque


def main():
    num_of_people, k = map(int, stdin.readline().split())
    table = deque([i for i in range(1, num_of_people + 1)])

    num_of_cycle = 0
    answer = []
    while table:
        num_of_cycle += 1
        if num_of_cycle == k:
            answer.append(table.popleft())
            num_of_cycle = 0
            continue
        table.append(table.popleft())

    answer_str = ''
    for idx, person in enumerate(answer):
        if idx == 0:
            answer_str += '<'
        answer_str += str(person)

        if idx != len(answer) - 1:
            answer_str += ', '

        if idx == len(answer) - 1:
            answer_str += '>'
    print(answer_str)


if __name__ == "__main__":
    main()
