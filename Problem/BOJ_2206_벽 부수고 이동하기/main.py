from sys import stdin
from collections import deque

moving_dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

stdin = open("./input.txt", "r")
rows, cols = map(int, stdin.readline().split())
matrix = []

for _ in range(rows):
    line = list(stdin.readline().rstrip())
    matrix.append(line)

visited = [[[False] * cols for _ in range(rows)] for _ in range(2)]


def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = True

    distance = 0
    while queue:
        size = len(queue)
        distance += 1
        for _ in range(size):
            cur_row, cur_col, count = queue.popleft()
            # print(cur_row, cur_col, count)

            if cur_row == rows - 1 and cur_col == cols - 1:
                return distance

            for moving_row, moving_col in moving_dir:
                next_row = cur_row + moving_row
                next_col = cur_col + moving_col
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if count == 0:
                        if matrix[next_row][next_col] == "1" and not visited[1][next_row][next_col]:
                            queue.append((next_row, next_col, count + 1))
                            visited[1][next_row][next_col] = True
                    if matrix[next_row][next_col] == "0" and not visited[count][next_row][next_col]:
                        queue.append((next_row, next_col, count))
                        visited[count][next_row][next_col] = True

    return -2


def main():
    distance = bfs()
    print(-1 if distance == -2 else distance)


if __name__ == '__main__':
    main()