from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 5)

moving_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(cur_row, cur_col, area):
    visited[cur_row][cur_col] = True

    for moving_row, moving_col in moving_dir:
        next_row = cur_row + moving_row
        next_col = cur_col + moving_col
        if 0 <= next_row < rows and 0 <= next_col < cols:
            if paper[next_row][next_col] == 0 and not visited[next_row][next_col]:
                area = dfs(next_row, next_col, area) + 1

    return area


def main():
    stdin = open("./input.txt", "r")
    global rows, cols, num_of_squares, paper, visited
    rows, cols, num_of_squares = map(int, stdin.readline().split())

    paper = [[0] * cols for _ in range(rows)]

    for _ in range(num_of_squares):
        x1, y1, x2, y2 = map(int, stdin.readline().split())

        for row in range(rows - y2, rows - y1):
            for col in range(x1, x2):
                paper[row][col] = 1

    # print(paper)
    visited = [[False] * cols for _ in range(rows)]

    num_of_area = 0
    areas = []
    for row in range(rows):
        for col in range(cols):
            if paper[row][col] == 0 and not visited[row][col]:
                num_of_area += 1
                areas.append(dfs(row, col, 1))

    print(num_of_area)

    areas.sort()
    print(' '.join(map(str, areas)))


if __name__ == '__main__':
    main()