from sys import stdin
from collections import deque

moving_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
moving_cheese = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]

stdin = open("./input.txt", "r")
rows, cols = map(int, stdin.readline().split())
plate = []
cheese_list = deque()

for _ in range(rows):
    plate.append(stdin.readline().split())

total_area = 0
for row in range(rows):
    for col in range(cols):
        if plate[row][col] == "1":
            total_area += 1


def bfs(start_row, start_col, target, is_change, change_value):
    queue = deque()
    queue.append((start_row, start_col))
    visited = [[False] * cols for _ in range(rows)]
    visited[start_row][start_col] = True

    area = -1
    while queue:
        size = len(queue)
        area += 1
        for _ in range(size):
            cur_row, cur_col = queue.popleft()
            if is_change:
                plate[cur_row][cur_col] = str(change_value)
            for moving_row, moving_col in moving_dir:
                next_row = cur_row + moving_row
                next_col = cur_col + moving_col
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if not visited[next_row][next_col] and plate[next_row][next_col] == target:
                        queue.append((next_row, next_col))
                        visited[next_row][next_col] = True
    return area


def melt(start_row, start_col, visited):
    queue = deque()
    queue.append((start_row, start_col))
    visited[start_row][start_col] = False

    while queue:
        cur_row, cur_col = queue.popleft()
        for cheese_row, cheese_col in moving_cheese:
            next_row = cur_row + cheese_row
            next_col = cur_col + cheese_col
            if 0 <= next_row < rows and 0 <= next_col < cols:




def main():
    bfs(0, 0, '0', True, 2)
    print(total_area)

    for row in plate:
        print(' '.join(row))


if __name__ == '__main__':
    main()