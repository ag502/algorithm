from sys import stdin


moving_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
rows, cols, time = 0, 0, 0
grid = None
bomb_time = None


def print_grid():
    for row in grid:
        print(''.join(row))


def install_bomb(cur_time):
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == ".":
                bomb_time[row][col] = cur_time + 3
                grid[row][col] = "O"


def explode_bomb(cur_time):
    for row in range(rows):
        for col in range(cols):
            if bomb_time[row][col] == cur_time:
                for moving_row, moving_col in moving_dir:
                    next_row = row + moving_row
                    next_col = col + moving_col
                    if 0 <= next_row < rows and 0 <= next_col < cols:
                        if grid[next_row][next_col] == "O":
                            grid[next_row][next_col] = "."
                grid[row][col] = "."
                bomb_time[row][col] = 0


def main():
    stdin = open("./input.txt", "r")
    global rows, cols, time, grid, bomb_time
    rows, cols, time = map(int, stdin.readline().split())

    grid = []
    for _ in range(rows):
        grid.append(list(stdin.readline().rstrip()))

    bomb_time = [[0] * cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "O":
                bomb_time[row][col] = 3

    if time == 0 or time == 1:
        print_grid()
    else:
        cur_time = 2
        install_bomb(2)
        while True:
            if cur_time == time:
                break
            cur_time += 1
            if cur_time % 2 == 1:
                explode_bomb(cur_time)
            else:
                install_bomb(cur_time)
        print_grid()


if __name__ == '__main__':
    main()