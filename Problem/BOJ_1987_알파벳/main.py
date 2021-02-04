from sys import stdin

moving_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

stdin = open("./input.txt", "r")
rows, cols = map(int, stdin.readline().split(" "))

board = []
for _ in range(rows):
    board.append(list(stdin.readline().rstrip()))

visited = [0] * 26


def travel_board(cur_row, cur_col):
    temp = 0
    cur_alphabet = board[cur_row][cur_col]
    visited[ord(cur_alphabet) - ord('A')] = 1

    for moving_row, moving_col in moving_dir:
        next_row = cur_row + moving_row
        next_col = cur_col + moving_col
        if 0 <= next_row < rows and 0 <= next_col < cols:
            if visited[ord(board[next_row][next_col]) - ord('A')] == 0:
                temp = max(temp, travel_board(next_row, next_col))

    visited[ord(cur_alphabet) - ord('A')] = 0
    return temp + 1


def main():
    print(travel_board(0, 0))


if __name__ == '__main__':
    main()