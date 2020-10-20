from sys import stdin, setrecursionlimit
from collections import deque
setrecursionlimit(1000000)

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def main():
    stdin = open("./test_case.txt", 'r')
    rows, cols = map(int, stdin.readline().split())
    icy = []

    for _ in range(rows):
        row = list(map(int, stdin.readline().split()))
        icy.append(row)

    year = 0
    while True:
        chunk = 0
        visited = [[False] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if icy[row][col] != 0 and not visited[row][col]:
                    chunk += 1
                    dfs(icy, row, col, rows, cols, visited)

        if chunk >= 2:
            print(year)
            return

        if chunk == 0:
            print(0)
            return

        melting(icy, rows, cols)
        year += 1


def melting(graph, rows, cols):
    queue = deque()
    for row in range(rows):
        for col in range(cols):
            if graph[row][col] != 0:
                num_of_sea = 0
                for moving_row, moving_col in directions:
                    if 0 <= row + moving_row < rows and 0 <= col + moving_col < cols:
                        if graph[row + moving_row][col + moving_col] == 0:
                            num_of_sea += 1

                queue.append([row, col, num_of_sea])

    while len(queue) != 0:
        cur_row, cur_col, cur_num_of_sea = queue.pop()
        if graph[cur_row][cur_col] - cur_num_of_sea < 0:
            graph[cur_row][cur_col] = 0
        else:
            graph[cur_row][cur_col] -= cur_num_of_sea

def dfs(graph, cur_row, cur_col, rows, cols, visited):
    # 방문
    visited[cur_row][cur_col] = True

    for moving_row, moving_col in directions:
        next_row = cur_row + moving_row
        next_col = cur_col + moving_col
        if 0 <= next_row < rows and 0 <= next_col < cols:
            if graph[next_row][next_col] != 0 and not visited[next_row][next_col]:
                dfs(graph, next_row, next_col, rows, cols, visited)

if __name__ == '__main__':
    main()