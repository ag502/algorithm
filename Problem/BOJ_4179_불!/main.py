from sys import stdin
from collections import deque

moving_dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

stdin = open("./input.txt", "r")
rows, cols = map(int, stdin.readline().split())

maze = []
for _ in range(rows):
    maze.append(list(stdin.readline().rstrip()))

start_pos = [0, 0]
visited = [[False] * cols for _ in range(rows)]
fire_pos = deque()

for row in range(rows):
    for col in range(cols):
        if maze[row][col] == "J":
            start_pos[0] = row
            start_pos[1] = col
        elif maze[row][col] == "F":
            fire_pos.append((row, col))


def move_fire():
    size = len(fire_pos)
    for _ in range(size):
        cur_fire_row, cur_fire_col = fire_pos.popleft()
        for moving_row, moving_col in moving_dir:
            next_f_row = cur_fire_row + moving_row
            next_f_col = cur_fire_col + moving_col
            if 0 <= next_f_row < rows and 0 <= next_f_col < cols:
                if maze[next_f_row][next_f_col] == ".":
                    maze[next_f_row][next_f_col] = "F"
                    fire_pos.append((next_f_row, next_f_col))


def bfs():
    queue = deque()
    queue.append((start_pos[0], start_pos[1]))
    visited[start_pos[0]][start_pos[1]] = True

    time = 0
    while queue:
        size = len(queue)
        time += 1
        for _ in range(size):
            cur_row, cur_col = queue.popleft()

            if maze[cur_row][cur_col] == "F":
                continue

            if cur_row == 0 or cur_row == rows - 1 or cur_col == 0 or cur_col == cols - 1:
                return time

            for moving_row, moving_col in moving_dir:
                next_row = cur_row + moving_row
                next_col = cur_col + moving_col
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if not visited[next_row][next_col] and maze[next_row][next_col] == ".":
                        queue.append((next_row, next_col))
                        visited[next_row][next_col] = True

        move_fire()

    return -2


def main():
    # print(maze)
    time = bfs()
    print("IMPOSSIBLE" if time == -2 else time)


if __name__ == '__main__':
    main()
