from sys import stdin
from collections import deque

#
# def bfs(connection, start, visited):
#     queue = deque()
#     queue.append(start)
#     visited[start] = True
#
#     hacked_computer = 0
#     while queue:
#         cur_computer = queue.popleft()
#         hacked_computer += 1
#
#         for next_computer in connection[cur_computer]:
#             if not visited[next_computer]:
#                 queue.append(next_computer)
#                 visited[next_computer] = True
#
#     return hacked_computer
#
#
# def main():
#     stdin = open("./input.txt", "r")
#     num_of_computers, num_of_relations = map(int, stdin.readline().split())
#
#     connections = {}
#     for computer in range(1, num_of_computers + 1):
#         connections[computer] = []
#
#     for _ in range(num_of_relations):
#         finish, start = map(int, stdin.readline().split())
#         connections[start].append(finish)
#
#     info = []
#     max_answer = 0
#     for start_computer in range(1, num_of_computers + 1):
#         visited = [0] * (num_of_computers + 1)
#         hacked_computer = bfs(connections, start_computer, visited)
#         max_answer = max(max_answer, hacked_computer)
#         info.append([start_computer, hacked_computer])
#
#     info.sort(key=lambda x: (-x[1], x[0]))
#     answer = []
#     for computer, value in info:
#         if value == max_answer:
#             answer.append(str(computer))
#
#     print(' '.join(answer))


def dfs(connections, start, visited):
    stack = deque()
    stack.append(start)
    visited[start] = 1

    hacked_computer = 0
    while stack:
        cur_computer = stack.pop()
        visited[cur_computer] = 2
        hacked_computer += 1

        for next_computer in connections[cur_computer]:
            if visited[next_computer] == 0:
                stack.append(next_computer)
                visited[next_computer] = 1

    return hacked_computer


def main():
    stdin = open("./input.txt", "r")
    num_of_computers, num_of_relations = map(int, stdin.readline().split())

    connections = {}
    for computer in range(1, num_of_computers + 1):
        connections[computer] = []

    for _ in range(num_of_relations):
        finish, start = map(int, stdin.readline().split())
        connections[start].append(finish)

    max_hacked = 0
    info = []
    for start_computer in range(1, num_of_computers + 1):
        visited = [0] * (num_of_computers + 1)
        hacked_computer = dfs(connections, start_computer, visited)
        max_hacked = max(max_hacked, hacked_computer)
        info.append(hacked_computer)

    answer = []
    for computer, value in enumerate(info):
        if value == max_hacked:
            answer.append(str(computer + 1))

    print(' '.join(answer))


if __name__ == "__main__":
    main()