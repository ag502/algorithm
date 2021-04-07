from sys import stdin, setrecursionlimit
from collections import deque
setrecursionlimit(10 ** 6)

moving_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

stdin = open("./input.txt", "r")
rows, cols = map(int, stdin.readline().split())
visited = [[False] * cols for _ in range(rows)]
array = []
area_list = deque()
check = set()

for _ in range(rows):
    array.append(list(map(int, stdin.readline().split())))


def bfs(cur_row, cur_col):
    queue = deque()
    queue.append((cur_row, cur_col))
    visited[cur_row][cur_col] = True

    area = 0
    while queue:
        cur_row, cur_col = queue.pop()
        area_list.append((cur_row, cur_col))
        area += 1

        for moving_row, moving_col in moving_dir:
            next_row = cur_row + moving_row
            next_col = cur_col + moving_col
            if 0 <= next_row < rows and 0 <= next_col < cols:
                if not visited[next_row][next_col] and array[next_row][next_col] == 1:
                    queue.append((next_row, next_col))
                    visited[next_row][next_col] = True
    return area


def main():
    answer = 0
    count = 0
    for row in range(rows):
        for col in range(cols):
            area_list.clear()
            if not visited[row][col] and array[row][col] == 1:
                count += 1
                area = bfs(row, col)
                answer = max(answer, area)
                for area_row, area_col in area_list:
                    array[area_row][area_col] = (area, count)

    for row in range(rows):
        for col in range(cols):
            if array[row][col] == 0:
                check.clear()
                temp = 0
                for moving_row, moving_col in moving_dir:
                    next_row = moving_row + row
                    next_col = moving_col + col
                    if 0 <= next_row < rows and 0 <= next_col < cols:
                        if array[next_row][next_col] != 0:
                            if array[next_row][next_col] not in check:
                                temp += array[next_row][next_col][0]
                                check.add(array[next_row][next_col])

                answer = max(answer, temp + 1)

    print(answer)


if __name__ == '__main__':
    main()