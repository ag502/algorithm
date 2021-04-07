from sys import stdin
from collections import deque

stdin = open("./input.txt", "r")

moving_dir = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
chess_board = []
for _ in range(8):
    chess_board.append(list(stdin.readline().rstrip()))

wall_positions = deque()
for row in range(8):
    for col in range(8):
        if chess_board[row][col] == "#":
            wall_positions.append([row, col])

visited = [[False] * 8 for _ in range(8)]


def move_wall():
    size = len(wall_positions)
    for _ in range(size):
        wall_row, wall_col = wall_positions.popleft()
        chess_board[wall_row][wall_col] = "."
        next_wall_row = wall_row + 1
        if 0 <= next_wall_row < 8:
            wall_positions.append((next_wall_row, wall_col))

    for wall_row, wall_col in wall_positions:
        chess_board[wall_row][wall_col] = "#"


def check_double(cur_row, cur_col):
    for wall_row, wall_col in wall_positions:
        if cur_row == wall_row and cur_col == wall_col:
            return False
    return True


def bfs():
    queue = deque()
    queue.append((7, 0))
    visited[7][0] = True

    while queue:
        size = len(queue)
        for _ in range(size):
            cur_row, cur_col = queue.popleft()

            if not check_double(cur_row, cur_col):
                visited[cur_row][cur_col] = False
                continue

            if cur_row == 0 and cur_col == 7:
                return 1

            queue.append((cur_row, cur_col))
            for moving_row, moving_col in moving_dir:
                next_row = cur_row + moving_row
                next_col = cur_col + moving_col
                if 0 <= next_row < 8 and 0 <= next_col < 8:
                    if not visited[next_row][next_col] and chess_board[next_row][next_col] == ".":
                        queue.append((next_row, next_col))
                        visited[next_row][next_col] = True
        move_wall()

    return 0


def main():
    print(bfs())


if __name__ == '__main__':
    main()