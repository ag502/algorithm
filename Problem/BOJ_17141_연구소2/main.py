from sys import stdin
from collections import deque
from itertools import combinations
from copy import deepcopy

moving_dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def bfs(lab, virus_pos, width):
    queue = deque()
    for row, col in virus_pos:
        queue.append([row, col])

    days = -1
    num_of_infection = 0
    while len(queue) != 0:
        size = len(queue)

        for _ in range(size):
            cur_row, cur_col = queue.popleft()
            for moving_row, moving_col in moving_dir:
                next_row = cur_row + moving_row
                next_col = cur_col + moving_col
                if 0 <= next_row < width and 0 <= next_col < width:
                    if lab[next_row][next_col] != 1 and lab[next_row][next_col] != -1:
                        queue.append([next_row, next_col])
                        lab[next_row][next_col] = -1
                        num_of_infection += 1
        days += 1
    return [days, num_of_infection]

def main():
    stdin = open('./input.txt', 'r')
    width, num_of_virus = map(int, stdin.readline().split())
    lab = []

    for _ in range(width):
        row = list(map(int, stdin.readline().split()))
        lab.append(row)

    virus_positions = []
    blank_area = 0
    for row in range(len(lab)):
        for col in range(len(lab[row])):
            if lab[row][col] == 2:
                virus_positions.append([row, col])
            if lab[row][col] != 1:
                blank_area += 1

    com_virus_pos = list(combinations(virus_positions, num_of_virus))

    answer = []
    for virus_pos in com_virus_pos:
        temp_lab = deepcopy(lab)
        for row, col in virus_pos:
            temp_lab[row][col] = -1
        days, num_of_infection = bfs(temp_lab, virus_pos, width)
        answer.append([days, num_of_infection])

    answer = sorted(answer, key=lambda x: (x[0]))

    for days, num_of_infection in answer:
        if num_of_infection + num_of_virus == blank_area:
            print(days)
            return
    print(-1)

if __name__ == '__main__':
    main()