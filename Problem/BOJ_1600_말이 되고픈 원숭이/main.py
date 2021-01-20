from sys import stdin
from collections import deque

monkey_moving = [[1, 0], [-1, 0], [0, 1], [0, -1]]
horse_moving = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]


def bfs(board, rows, cols, cur_row, cur_col, max_horse_moving_count):
    queue = deque()
    queue.append([max_horse_moving_count, cur_row, cur_col])
    board[cur_row][cur_col] = -1

    moving_count = 0
    while len(queue) != 0:
        size = len(queue)
        for _ in range(size):
            horse_moving_count, cur_row, cur_col = queue.popleft()
            print(horse_moving_count, cur_row, cur_col)

            if cur_row == rows - 1 and cur_col == cols - 1:
                return moving_count

            for moving_row, moving_col in monkey_moving:
                next_row = cur_row + moving_row
                next_col = cur_col + moving_col
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if board[next_row][next_col] == 0:
                        queue.append([horse_moving_count, next_row, next_col])
                        board[next_row][next_col] = -1

            if horse_moving_count > 0:
                for moving_row, moving_col in horse_moving:
                    next_row = cur_row + moving_row
                    next_col = cur_col + moving_col
                    if 0 <= next_row < rows and 0 <= next_col < cols:
                        if board[next_row][next_col] == 0:
                            queue.append([horse_moving_count - 1, next_row, next_col])
                            board[next_row][next_col] = -1

        moving_count += 1
    return -1


def main():
    stdin = open('./input.txt', 'r')
    horse_move_count = int(stdin.readline())
    cols, rows = map(int, stdin.readline().split())

    board = []
    for _ in range(rows):
        row = list(map(int, stdin.readline().split()))
        board.append(row)

    # print(board)

    distance = bfs(board, rows, cols, 0, 0, horse_move_count)

    for row in range(rows):
        print(board[row])

    print(distance)


if __name__ == '__main__':
    main()