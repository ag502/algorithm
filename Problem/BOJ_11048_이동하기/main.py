from sys import stdin

moving_dir = [[0, 1], [1, 0], [1, 1]]


def main():
    stdin = open("./input.txt", "r")
    rows, cols = map(int, stdin.readline().split())

    maze = []
    for _ in range(rows):
        maze.append(list(map(int, stdin.readline().split())))

    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = maze[0][0]

    for row in range(rows):
        for col in range(cols):
            for moving_row, moving_col in moving_dir:
                next_row = row + moving_row
                next_col = col + moving_col
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    dp[next_row][next_col] = max(dp[next_row][next_col], maze[next_row][next_col] + dp[row][col])

    print(dp[rows - 1][cols - 1])


if __name__ == '__main__':
    main()