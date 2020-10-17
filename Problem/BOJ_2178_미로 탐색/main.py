from sys import stdin
from collections import deque

moving_row_dist = [-1, 0, 1, 0]
moving_col_dist = [0, 1, 0, -1]

def main():
    file = open("./test_case.txt", 'r')
    rows, cols = map(int, file.readline().split())
    maze = [[0] * (cols + 1)]
    pq = deque()

    for _ in range(rows):
        row = [0] + list(map(int, list(file.readline().rstrip())))
        maze.append(row)

    file.close()

    pq.append([1, 1])
    maze[1][1] = -1
    answer = 0

    while len(pq) != 0:
        size = len(pq)
        answer += 1
        for _ in range(size):
            cur_pos_row, cur_pos_col = pq.popleft()
            if cur_pos_row == rows and cur_pos_col == cols:
                print(answer)
                return
            # 갈 수 있는 지점 탐색
            for moving_row, moving_col in zip(moving_row_dist, moving_col_dist):
                next_pos_row = cur_pos_row + moving_row
                next_pos_col = cur_pos_col + moving_col
                if 1 <= next_pos_row <= rows and 1 <= next_pos_col <= cols:
                    if maze[next_pos_row][next_pos_col] == 1:
                        pq.append([next_pos_row, next_pos_col])
                        maze[next_pos_row][next_pos_col] = -1

if __name__ == '__main__':
    main()