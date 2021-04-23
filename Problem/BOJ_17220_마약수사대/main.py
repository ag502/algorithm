from sys import stdin
from collections import deque

stdin = open("./input.txt", "r")
num_of_criminal, num_of_relation = map(int, stdin.readline().split())

relations = {}
parents = {}
for i in range(0, num_of_criminal):
    relations[chr(ord('A') + i)] = []
    parents[chr(ord('A') + i)] = chr(ord('A') + i)

for _ in range(num_of_relation):
    criminal1, criminal2 = stdin.readline().rstrip().split()
    relations[criminal1].append(criminal2)
    parents[criminal2] = criminal1

catch_criminal = set(list(stdin.readline().split())[1:])
visited = [False] * 26
count = 0


def dfs(cur_criminal):
    global count
    visited[ord(cur_criminal) - ord('A')] = True
    count += 1
    for next_criminal in relations[cur_criminal]:
        if not visited[ord(next_criminal) - ord('A')] and next_criminal not in catch_criminal:
            dfs(next_criminal)


def main():
    start = []
    for parent, child in parents.items():
        if parent == child:
            start.append(parent)

    for a in list(catch_criminal):
        relations[a] = []

    global count
    answer = 0
    for parent in start:
        count = 0
        dfs(parent)
        answer += count - 1
    print(answer)


if __name__ == '__main__':
    main()