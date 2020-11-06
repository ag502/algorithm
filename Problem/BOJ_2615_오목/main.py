from sys import stdin

moving_dir = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

def is_in_board(row, col, moving_row, moving_col):
    next_row = row + moving_row
    next_col = col + moving_col
    if 0 <= next_row < 19 and 0 <= next_col < 19:
        return True
    return False

def main():
    stdin = open('./test_case.txt', 'r')
    board = []
    for _ in range(19):
        row = list(map(int, stdin.readline().split()))
        board.append(row)

    for row in range(19):
        for col in range(19):
            if board[row][col] == 1:
                for moving_row, moving_col in moving_dir:
                    cur_row = row
                    cur_col = col
                    count = 1
                    top = [(cur_row, cur_col)]
                    while is_in_board(cur_row, cur_col, moving_row, moving_col) and \
                        board[cur_row + moving_row][cur_col + moving_col] == 1:
                        count += 1
                        cur_row += moving_row
                        cur_col += moving_col
                        top.append((cur_row, cur_col))
                    if count == 5:
                        if is_in_board(top[0][0], top[0][1], -moving_row, -moving_col):
                            if board[top[0][0] - moving_row][top[0][1] - moving_col] == 1:
                                continue
                        print(1)
                        top = sorted(top, key=lambda x: (x[1], x[0]))
                        print(str(top[0][0] + 1) + " " + str(top[0][1] + 1))
                        return
            elif board[row][col] == 2:
                for moving_row, moving_col in moving_dir:
                    count = 1
                    cur_row = row
                    cur_col = col
                    top = [(cur_row, cur_col)]
                    while is_in_board(cur_row, cur_col, moving_row, moving_col) and \
                        board[cur_row + moving_row][cur_col + moving_col] == 2:
                        count += 1
                        cur_row += moving_row
                        cur_col += moving_col
                        top.append((cur_row, cur_col))
                    if count == 5:
                        if is_in_board(top[0][0], top[0][1], -moving_row, -moving_col):
                            if board[top[0][0] - moving_row][top[0][1] - moving_col] == 2:
                                continue
                        print(2)
                        top = sorted(top, key=lambda x: (x[1], x[0]))
                        print(str(top[0][0] + 1) + " " + str(top[0][1] + 1))
                        return
    print(0)
if __name__ == '__main__':
    main()