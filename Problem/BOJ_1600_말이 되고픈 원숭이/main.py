from sys import stdin
from collections import deque

moving_monkey = [[1, 0], [-1, 0], [0, 1], [0, -1]]
moving_horse = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

stdin = open("./input.txt", "r")
k = int(stdin.readline())
cols, rows = map(int, stdin.readline().split())
grid = []

for _ in range(rows):
    grid.append(stdin.readline().split())

visited = [[[False] * cols for _ in range(rows)] for _ in range(k + 1)]


def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = True

    distance = -1
    while queue:
        size = len(queue)
        distance += 1
        for _ in range(size):
            cur_row, cur_col, horse_count = queue.popleft()
            # print(cur_row, cur_col, horse_count)

            if cur_row == rows - 1 and cur_col == cols - 1:
                return distance

            for monkey_row, monkey_col in moving_monkey:
                next_row = cur_row + monkey_row
                next_col = cur_col + monkey_col
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if not visited[horse_count][next_row][next_col] and grid[next_row][next_col] == "0":
                        queue.append((next_row, next_col, horse_count))
                        visited[horse_count][next_row][next_col] = True

            if horse_count < k:
                for horse_row, horse_col in moving_horse:
                    next_row = cur_row + horse_row
                    next_col = cur_col + horse_col
                    if 0 <= next_row < rows and 0 <= next_col < cols:
                        if not visited[horse_count + 1][next_row][next_col] and grid[next_row][next_col] == "0":
                            queue.append((next_row, next_col, horse_count + 1))
                            visited[horse_count + 1][next_row][next_col] = True

    return -2


def main():
    distance = bfs()
    print(-1 if distance == -2 else distance)


if __name__ == '__main__':
    main()