from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 4)

moving_dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(graph_paper, rows, cols, cur_row, cur_col, area_size):
    # 1. 방문
    graph_paper[cur_row][cur_col] = -1
    # 2. 갈 수 있는곳 탐색
    for moving_row, moving_col in moving_dir:
        next_row = cur_row + moving_row
        next_col = cur_col + moving_col
        if 0 <= next_row < rows and 0 <= next_col < cols:
            if graph_paper[next_row][next_col] == 0:
                # 3. 간다
                area_size = dfs(graph_paper, rows, cols, next_row, next_col, area_size) + 1
    return area_size


def main():
    stdin = open('./input.txt', 'r')
    rows, cols, num_of_squares = map(int, stdin.readline().split())

    graph_paper = [[0] * cols for _ in range(rows)]

    for _ in range(num_of_squares):
        x1, y1, x2, y2 = map(int, stdin.readline().split())

        for row in range(rows - y2, rows - y1):
            for col in range(x1, x2):
                graph_paper[row][col] = 1

    num_of_area = 0
    areas = []
    for row in range(rows):
        for col in range(cols):
            if graph_paper[row][col] == 0:
                num_of_area += 1
                areas.append(dfs(graph_paper, rows, cols, row, col, 1))

    print(num_of_area)
    print(' '.join(map(str, sorted(areas))))


if __name__ == '__main__':
    main()
