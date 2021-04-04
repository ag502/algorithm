from sys import stdin
from collections import deque


moving_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def print_grid(init_grid):
    for row in init_grid:
        print(''.join(row))


def install_bomb(bomb_row):
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == ".":
                bombs[bomb_row].append((row, col))
                except_bombs[bomb_row].add((row, col))
                grid[row][col] = "O"


def explode_bomb(bomb_row):
    while bombs[bomb_row]:
        cur_row, cur_col = bombs[bomb_row].popleft()
        temp = (cur_row, cur_col)
        if temp in except_bombs[bomb_row]:
            grid[cur_row][cur_col] = "."
            for moving_row, moving_col in moving_dir:
                next_row = cur_row + moving_row
                next_col = cur_col + moving_col
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    grid[next_row][next_col] = '.'
                except_bombs[(bomb_row + 1) % 2].discard((next_row, next_col))
            except_bombs[bomb_row].discard((cur_row, cur_col))


def main():
    stdin = open("./input.txt", "r")
    global rows, cols, time, grid, bombs, except_bombs
    rows, cols, time = map(int, stdin.readline().split())
    grid = []

    for _ in range(rows):
        row = list(stdin.readline().rstrip())
        grid.append(row)

    bombs = [deque(), deque()]
    except_bombs = [set(), set()]

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "O":
                bombs[0].append((row, col))
                except_bombs[0].add((row, col))

    if time == 0 or time == 1:
        print_grid(grid)
    else:
        cur_time = 2
        install_bomb(1)
        flag = True
        while True:
            if cur_time == time:
                break
            cur_time += 1
            if cur_time % 2 == 1:
                if flag:
                    explode_bomb(0)
                else:
                    explode_bomb(1)
            elif cur_time % 2 == 0:
                if flag:
                    install_bomb(0)
                else:
                    install_bomb(1)
                flag = not flag
        print_grid(grid)


if __name__ == '__main__':
    main()