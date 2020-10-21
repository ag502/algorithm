from sys import stdin, setrecursionlimit
from collections import deque
setrecursionlimit(10000)

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def main():
    # stdin = open("./test_case.txt", 'r')
    rows, cols = map(int, stdin.readline().split())
    icy = []

    for _ in range(rows):
        row = list(map(int, stdin.readline().split()))
        icy.append(row)

    queue = deque()
    year = 0
    while True:
        visited = [[False] * cols for _ in range(rows)]
        queue.clear()
        chunk = 0
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

        melt(icy, rows, cols)
        year += 1

def melt(graph, rows, cols):
    visited = [[False] * cols for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            num_of_sea = 0
            for moving_row, moving_col in directions:
                sea_row = row + moving_row
                sea_col = col + moving_col
                if 0 <= sea_row < rows and 0 <= sea_col < cols:
                    if not visited[sea_row][sea_col] and graph[sea_row][sea_col] == 0:
                        num_of_sea += 1
            if graph[row][col] > 0:
                graph[row][col] = max(0, graph[row][col] - num_of_sea)
                visited[row][col] = True

def dfs(graph, cur_row, cur_col, rows, cols, visited):
    visited[cur_row][cur_col] = True

    for moving_row, moving_col in directions:
        next_row = cur_row + moving_row
        next_col = cur_col + moving_col
        if 0 <= next_row < rows and 0 <= next_col < cols:
            if not visited[next_row][next_col] and graph[next_row][next_col] != 0:
                dfs(graph, next_row, next_col, rows, cols, visited)

if __name__ == '__main__':
    main()