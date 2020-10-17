from sys import stdin
from collections import deque

def main():
    # stdin = open('./test_case.txt', 'r')

    boxes = []
    cols, rows, height = map(int, stdin.readline().split())

    moving_row = [ -1, 0, 1, 0]
    moving_col = [ 0, 1, 0, -1]
    moving_hei = [-1, 1]

    for _ in range(height):
        box = []
        for _ in range(rows):
            row = list(map(int, stdin.readline().split()))
            box.append(row)
        boxes.append(box)
    # print(boxes)
    queue = deque()
    total_tomato = 0
    ripped_tomato = 0

    for i in range(height):
        for row in range(rows):
            for col in range(cols):
                if boxes[i][row][col] == 0 or boxes[i][row][col] == 1:
                    total_tomato += 1
                    if boxes[i][row][col] == 1:
                        ripped_tomato += 1
                        # row, col, height
                        queue.append([row, col, i])

    day = -1
    while len(queue) != 0:
        size = len(queue)
        day += 1
        for _ in range(size):
            cur_row, cur_col, cur_height = queue.popleft()
            # 갈 수 있는 토마토 장소 탐색
            for moving_row_dir, moving_col_dir in zip(moving_row, moving_col):
                next_row = cur_row + moving_row_dir
                next_col = cur_col + moving_col_dir
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if boxes[cur_height][next_row][next_col] == 0:
                        boxes[cur_height][next_row][next_col] = 1
                        queue.append([next_row, next_col, cur_height])
                        ripped_tomato += 1

            for moving_height_dir in moving_hei:
                next_height = cur_height + moving_height_dir
                if 0 <= next_height < height:
                    if boxes[next_height][cur_row][cur_col] == 0:
                        boxes[next_height][cur_row][cur_col] = 1
                        queue.append([cur_row, cur_col, next_height])
                        ripped_tomato += 1

    print(day if ripped_tomato == total_tomato else -1)

if __name__ == '__main__':
    main()