from sys import stdin
from collections import deque

moving_dir_row = [1, -1, 0, 0]
moving_dir_col = [0, 0, 1, -1]

def main():
    cols, rows = map(int, stdin.readline().split())
    queue = deque()
    field = []

    for _ in range(rows):
        field_row = list(map(int, stdin.readline().split()))
        field.append(field_row)

    total_tomato = 0
    riped_tomato = 0
    for row in range(rows):
        for col in range(cols):
            if field[row][col] == 1:
                queue.append([row, col])
                # riped_tomato += 1
            if field[row][col] != -1:
                total_tomato += 1


    days = 0
    while len(queue) != 0:
        size = len(queue)
        for i in range(size):
            cur_pos_row, cur_pos_col = queue.popleft()
            riped_tomato += 1
            for moving_row, moving_col in zip(moving_dir_row, moving_dir_col):
                can_go_row = cur_pos_row + moving_row
                can_go_col = cur_pos_col + moving_col
                if 0 <= can_go_row < rows and 0 <= can_go_col < cols:
                    if field[can_go_row][can_go_col] == 0:
                        queue.append([can_go_row, can_go_col])
                        field[can_go_row][can_go_col] = 1

        days += 1

    if riped_tomato == total_tomato:
        print(days - 1)
    else:
        print(-1)

if __name__ == '__main__':
    main()
