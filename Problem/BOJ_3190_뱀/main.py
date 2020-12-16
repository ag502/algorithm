from sys import stdin
from collections import deque

def change_dir(dir_queue, command):
    if command == 'D':
        dir_queue.appendleft(dir_queue.pop())
    elif command == 'L':
        dir_queue.append(dir_queue.popleft())

def main():
    stdin = open('./input.txt', 'r')

    # 보드 초기화
    board_width = int(stdin.readline())
    board = [[0] * (board_width + 1) for _ in range(board_width + 1)]

    # 사과 위치 지정
    num_of_apples = int(stdin.readline())
    for _ in range(num_of_apples):
        x, y = map(int, stdin.readline().split())
        board[x][y] = 1

    # 명령어
    commands = {}
    num_of_commands = int(stdin.readline())
    for _ in range(num_of_commands):
        seconds, direction = stdin.readline().split()
        commands[int(seconds)] = direction

    dir_queue = deque([[0, 1], [-1, 0], [0, -1], [1, 0]])
    snake = deque([[1, 1]])

    second = 0
    while True:
        # 명령어 확인
        if second in commands:
            change_dir(dir_queue, commands[second])
        cur_dir = dir_queue[0]

        # 뱀 이동
        next_row = snake[0][0] + cur_dir[0]
        next_col = snake[0][1] + cur_dir[1]
        snake.appendleft([next_row, next_col])

        snake_head_x, snake_head_y = snake[0]
        # 게임 오버
        if  1 > snake_head_x or snake_head_x > board_width or \
            1 > snake_head_y or snake_head_y > board_width or \
            board[snake_head_x][snake_head_y] == -1:
            print(second + 1)
            return
        else:
            if board[snake_head_x][snake_head_y] == 0:
                snake_tail_x, snake_tail_y = snake.pop()
                board[snake_tail_x][snake_tail_y] = 0
            board[snake_head_x][snake_head_y] = -1
        second += 1

if __name__ == '__main__':
    main()
