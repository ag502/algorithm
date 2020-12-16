from sys import stdin
from collections import deque

moving_dir = {
    1: [0, 1],
    2: [0, -1],
    3: [-1, 0],
    4: [1, 0]
}

def process_number(board, dice, cur_row, cur_col):
    board_number = board[cur_row][cur_col]
    if board_number == 0:
        board[cur_row][cur_col] = dice[2][1]
    else:
        dice[2][1] = board[cur_row][cur_col]
        board[cur_row][cur_col] = 0

def main():
    stdin = open('./input.txt', 'r')
    rows, cols, dice_x, dice_y, num_of_commands = map(int, stdin.readline().split())

    board = []
    for _ in range(rows):
        board.append(list(map(int, stdin.readline().split())))

    commands = list(map(int, stdin.readline().split()))

    dice_vertical = deque([[1, 0], [5, 0], [6, 0], [2, 0]])
    dice_horizontal = deque([[1, 0], [3, 0], [6, 0], [4, 0]])

    for command in commands:
        moving_row, moving_col = moving_dir[command]
        next_row = dice_x + moving_row
        next_col = dice_y + moving_col
        if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
            continue
        dice_x = next_row
        dice_y = next_col

        # 주사위 굴리기
        if command in [3, 4]:
            if command == 3:
                dice_vertical.append(dice_vertical.popleft())
            elif command == 4:
                dice_vertical.appendleft(dice_vertical.pop())
            process_number(board, dice_vertical, dice_x, dice_y)
            dice_horizontal[0] = dice_vertical[0]
            dice_horizontal[2] = dice_vertical[2]
            print(dice_vertical[0][1])
        elif command in [1, 2]:
            if command == 1:
                dice_horizontal.appendleft(dice_horizontal.pop())
            elif command == 2:
                dice_horizontal.append(dice_horizontal.popleft())
            process_number(board, dice_horizontal, dice_x, dice_y)
            dice_vertical[0] = dice_horizontal[0]
            dice_vertical[2] = dice_horizontal[2]
            print(dice_horizontal[0][1])

if __name__ == '__main__':
    main()