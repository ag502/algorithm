from sys import stdin, setrecursionlimit
setrecursionlimit(100000)

moving_row = [-1, 0, 1, 0]
moving_col = [0, 1, 0, -1]

def main():
    # stdin = open('./test_case.txt', 'r')
    n = int(stdin.readline())

    areas = []
    for _ in range(n):
        row = list(map(int, stdin.readline().split()))
        areas.append(row)

    max_height = 0
    for row in range(n):
        for col in range(n):
            if max_height < areas[row][col]:
                max_height = areas[row][col]

    answer = 0
    for height in range(0, max_height + 1):
        visited = [[False] * n for _ in range(n)]
        num_of_area = 0
        for i in range(n):
            for j in range(n):
                if areas[i][j] > height and not visited[i][j]:
                    num_of_area += 1
                    dfs(areas, visited, i, j, height, n)
        answer = max(answer, num_of_area)
    print(answer)

def dfs(graph, visited, cur_row, cur_col, height, n):
    # 방문
    visited[cur_row][cur_col] = True
    # 갈 수 있는 곳 탐색
    for moving_row_dir, moving_col_dir in zip(moving_row, moving_col):
        next_row = cur_row + moving_row_dir
        next_col = cur_col + moving_col_dir
        if 0 <= next_row < n and 0 <= next_col < n:
            if graph[next_row][next_col] > height and not visited[next_row][next_col]:
                dfs(graph, visited, next_row, next_col, height, n)

if __name__ == '__main__':
    main()