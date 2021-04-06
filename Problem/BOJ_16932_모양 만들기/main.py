from sys import stdin

moving_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

stdin = open("./input.txt", "r")
rows, cols = map(int, stdin.readline().split())
zero_list = []
array = []

for _ in range(rows):
    first_line = list(map(int, stdin.readline().split()))
    array.append(first_line)

for row in range(rows):
    for col in range(cols):
        if array[row][col] == 0:
            zero_list.append((row, col))


def dfs(cur_row, cur_col, area, visited):
    visited[cur_row][cur_col] = True

    for moving_row, moving_col in moving_dir:
        next_row = cur_row + moving_row
        next_col = cur_col + moving_col
        if 0 <= next_row < rows and 0 <= next_col < cols:
            if not visited[next_row][next_col] and array[next_row][next_col] == 1:
                area = dfs(next_row, next_col, area + 1, visited)
    return area


def main():
    answer = 0
    for zero_row, zero_col in zero_list:
        visited = [[False] * cols for _ in range(rows)]
        array[zero_row][zero_col] = 1
        for row in range(rows):
            for col in range(cols):
                if not visited[row][col] and array[row][col] == 1:
                    answer = max(answer, dfs(row, col, 1, visited))
        array[zero_row][zero_col] = 0

    print(answer)


if __name__ == '__main__':
    main()