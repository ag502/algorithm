from sys import stdin
from collections import deque

stdin = open("./input.txt", "r")

moving_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

rows, cols = map(int, stdin.readline().split())
answer = [["0"] * cols for _ in range(rows)]
graph = []
for _ in range(rows):
    graph.append(stdin.readline().split())
destination_pos = []


def bfs(start_row, start_col, visited):
    queue = deque()
    queue.append((start_row, start_col))
    visited[start_row][start_col] = True

    distance = 0
    while queue:
        size = len(queue)

        distance += 1
        for _ in range(size):
            cur_row, cur_col = queue.popleft()
            answer[cur_row][cur_col] = str(distance - 1)

            for moving_row, moving_col in moving_dir:
                next_row = cur_row + moving_row
                next_col = cur_col + moving_col
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if not visited[next_row][next_col] and graph[next_row][next_col] != "0":
                        queue.append((next_row, next_col))
                        visited[next_row][next_col] = True


def main():
    for row in range(rows):
        for col in range(cols):
            if graph[row][col] == "2":
                destination_pos.append(row)
                destination_pos.append(col)

    visited = [[False] * cols for _ in range(rows)]
    bfs(destination_pos[0], destination_pos[1], visited)

    for row in range(rows):
        for col in range(cols):
            if answer[row][col] == "0" and graph[row][col] == "1":
                answer[row][col] = "-1"

    for row in answer:
        print(' '.join(row))


if __name__ == '__main__':
    main()