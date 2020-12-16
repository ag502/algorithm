from sys import stdin
from collections import deque
from itertools import combinations
from copy import deepcopy

moving_dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def bfs(labs, wall_pos, virus_pos, rows, cols):
    copy_labs = deepcopy(labs)
    for row, col in wall_pos:
        copy_labs[row][col] = 1

    queue = deque()
    for pos in virus_pos:
        queue.append(pos)

    while len(queue) != 0:
        cur_row, cur_col = queue.popleft()

        for moving_row, moving_col in moving_dir:
            next_row = cur_row + moving_row
            next_col = cur_col + moving_col
            if 0 <= next_row < rows and 0 <= next_col < cols:
                if copy_labs[next_row][next_col] == 0:
                    copy_labs[next_row][next_col] = 2
                    queue.append((next_row, next_col))
    return copy_labs

def main():
    stdin = open('./input.txt', 'r')
    rows, cols = map(int, stdin.readline().split())

    # 연구실 초기화
    labs = []
    for _ in range(rows):
        labs.append(list(map(int, stdin.readline().split())))

    # 벽을 세울 수 있는 위치 탐색 / 바이러스 위치 탐색
    vacancy_pos = []
    virus_pos = []
    for row in range(rows):
        for col in range(cols):
            if labs[row][col] == 0:
                vacancy_pos.append((row, col))
            if labs[row][col] == 2:
                virus_pos.append((row, col))

    # 벽을 세울 수 있는 위치 목록
    new_wall_pos = list(combinations(vacancy_pos, 3))

    safety_area = []
    for wall_pos in new_wall_pos:
        area = 0
        after_labs = bfs(labs, wall_pos, virus_pos, rows, cols)
        for row in range(rows):
            for col in range(cols):
                if after_labs[row][col] == 0:
                    area += 1
        safety_area.append(area)
    print(max(safety_area))

if __name__ == '__main__':
    main()