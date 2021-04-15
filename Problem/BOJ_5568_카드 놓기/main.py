from sys import stdin
from collections import deque

stdin = open("./input.txt", "r")
num_of_cards = int(stdin.readline())
num_of_choose = int(stdin.readline())
cards = []

for _ in range(num_of_cards):
    cards.append(int(stdin.readline()))

answer = set()


def dfs(cur_idx, visited, temp):
    visited[cur_idx] = True
    temp.append(cards[cur_idx])

    if len(temp) < num_of_choose:
        for next_idx in range(num_of_cards):
            if not visited[next_idx]:
                dfs(next_idx, visited, temp)
    elif len(temp) == num_of_choose:
        answer.add(''.join(map(str, temp)))
    temp.pop()
    visited[cur_idx] = False


def main():
    visited = [False] * num_of_cards
    for idx in range(num_of_cards):
        if not visited[idx]:
            dfs(idx, visited, deque())

    print(len(answer))


if __name__ == '__main__':
    main()