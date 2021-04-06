from sys import stdin
from collections import deque

moving_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


stdin = open("./input.txt", "r")
rows, cols = map(int, stdin.readline().split())
grid = [[0] * (cols + 1)]

for _ in range(rows):
    line = [0] + list(map(int, stdin.readline().split()))
    grid.append(line)

height, width, start_row, start_col, finish_row, finish_col = map(int, stdin.readline().split())
visited = [[False] * (cols + 1) for _ in range(rows + 1)]


def bfs():
    queue = deque()
    queue.append((start_row, start_col))
    visited[start_row][start_col] = True

    time = -1
    while queue:
        size = len(queue)
        time += 1
        for _ in range(size):
            cur_row, cur_col = queue.popleft()
            if cur_row == finish_row and cur_col == finish_col:
                return time

            for idx, (moving_row, moving_col) in enumerate(moving_dir):
                next_row = moving_row + cur_row
                next_col = moving_col + cur_col
                if 1 <= next_row <= rows - height + 1 and 1 <= next_col <= cols - width + 1 and not visited[next_row][next_col] and grid[next_row][next_col] == 0:
                    total = 0
                    if idx == 0:
                        total = sum(grid[next_row + height - 1][next_col:next_col + width])
                    elif idx == 1:
                        total = sum(grid[next_row][next_col:next_col + width])
                    elif idx == 2:
                        for row in range(next_row, next_row + height):
                            total += grid[row][next_col + width - 1]
                    else:
                        for row in range(next_row, next_row + height):
                            total += grid[row][next_col]

                    if total == 0:
                        queue.append((next_row, next_col))
                        visited[next_row][next_col] = True

    return -2


def main():
    time = bfs()
    print(-1 if time == -2 else time)


if __name__ == '__main__':
    main()