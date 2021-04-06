from sys import stdin
from collections import deque

moving_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

stdin = open("./input.txt", "r")
rows, cols, time_limit = map(int, stdin.readline().split())
cattle = []

for _ in range(rows):
    line = list(map(int, stdin.readline().split()))
    cattle.append(line)

visited = [[[False] * cols for _ in range(rows)] for _ in range(2)]


def bfs(start_row, start_col):
    queue = deque()
    queue.append((start_row, start_col, False))
    visited[0][start_row][start_col] = True

    time = -1
    while queue:
        size = len(queue)
        time += 1
        for _ in range(size):
            cur_row, cur_col, get_sword = queue.popleft()

            if time > time_limit:
                return -2

            if cur_row == rows - 1 and cur_col == cols - 1:
                return time

            for moving_row, moving_col in moving_dir:
                next_row = cur_row + moving_row
                next_col = cur_col + moving_col
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if get_sword:
                        if not visited[1][next_row][next_col]:
                            visited[1][next_row][next_col] = True
                            queue.append((next_row, next_col, True))
                    else:
                        if not visited[0][next_row][next_col] and cattle[next_row][next_col] != 1:
                            if cattle[next_row][next_col] == 2:
                                visited[1][next_row][next_col] = True
                                queue.append((next_row, next_col, True))
                            else:
                                visited[0][next_row][next_col] = True
                                queue.append((next_row, next_col, False))

    return -2


def main():
    time = bfs(0, 0)
    print("Fail" if time == -2 else time)


if __name__ == '__main__':
    main()