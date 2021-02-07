from sys import stdin

stdin = open("./input.txt", "r")
length_of_board = int(stdin.readline())
answer = [0]
visited = [-1] * length_of_board


def is_possible(next_row, next_col):
    for row in range(next_row):
        if row == next_row:
            return False
        if visited[row] == next_col:
            return False
        if abs(row - next_row) == abs(next_col - visited[row]):
            return False
    return True


def positioning_queen(cur_queen, cur_row, cur_col):
    visited[cur_row] = cur_col

    if cur_queen < length_of_board:
        for next_col in range(length_of_board):
            if is_possible(cur_row + 1, next_col):
                positioning_queen(cur_queen + 1, cur_row + 1, next_col)

    if cur_queen == length_of_board:
        answer[0] += 1
    visited[cur_row] = -1


def main():
    for col in range(length_of_board):
        positioning_queen(1, 0, col)
    print(answer[0])


if __name__ == '__main__':
    main()