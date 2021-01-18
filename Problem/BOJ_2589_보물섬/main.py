from sys import stdin
from collections import deque

moving_dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def bfs(treasure_map, rows, cols, cur_row, cur_col, visited):
    queue = deque()
    queue.append([cur_row, cur_col])
    visited[cur_row][cur_col] = True

    distance = -1
    while len(queue) != 0:
        size = len(queue)

        for _ in range(size):
            cur_row, cur_col = queue.popleft()
            for moving_row, moving_col in moving_dir:
                next_row = cur_row + moving_row
                next_col = cur_col + moving_col
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if treasure_map[next_row][next_col] == 'L' and not visited[next_row][next_col]:
                        queue.append([next_row, next_col])
                        visited[next_row][next_col] = True

        distance += 1

    return distance


def main():
    stdin = open('./input.txt', 'r')
    rows, cols = map(int, stdin.readline().split())

    treasure_map = []
    for _ in range(rows):
        row = list(stdin.readline().strip())
        treasure_map.append(row)

    distance = 0
    for row in range(rows):
        for col in range(cols):
            visited = [[False] * cols for _ in range(rows)]
            if treasure_map[row][col] == 'L':
                # print(row, col)
                # print(bfs(treasure_map, rows, cols, row, col, visited))
                distance = max(distance, bfs(treasure_map, rows, cols, row, col, visited))

    print(distance)


if __name__ == '__main__':
    main()