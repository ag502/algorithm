from sys import stdin

# [row, col]
moving_dir = {
    'R': [0, 1], 'L': [0, -1], 'B': [1, 0], 'T': [-1, 0],
    'RT': [-1, 1], 'LT': [-1, -1], 'RB': [1, 1], 'LB': [1, -1]
}

def convert_pos(position, type):
    col, row = position
    if type == "CHAR_TO_NUM":
        return [ord(col) - ord('A'), 8 - int(row)]
    elif type == "NUM_TO_CHAR":
        return chr(ord('A') + col) + str(8 - row)

def is_in_board(col, row, moving_dist):
    moving_row, moving_col = moving_dist
    next_row = row + moving_row
    next_col = col + moving_col
    if 0 <= next_row < 8 and 0 <= next_col < 8:
        return True
    return False

def main():
    stdin = open('./test_case.txt', 'r')
    king_pos, stone_pos, num_of_moving = stdin.readline().split()

    king_cur_col, king_cur_row = convert_pos(list(king_pos), 'CHAR_TO_NUM')
    stone_cur_col, stone_cur_row = convert_pos(list(stone_pos), 'CHAR_TO_NUM')

    for _ in range(int(num_of_moving)):
        direction = stdin.readline().rstrip()
        moving_dist = moving_dir[direction]

        # king이 움직일 위치가 보드 안에 있는가?
        if is_in_board(king_cur_col, king_cur_row, moving_dist):
            next_king_row = king_cur_row +  moving_dist[0]
            next_king_col = king_cur_col + moving_dist[1]
            # king과 돌이 겹칠 때
            if next_king_row == stone_cur_row and next_king_col == stone_cur_col:
                # 돌이 움직일 위치가 보드 안에 있는가?
                if is_in_board(stone_cur_col, stone_cur_row, moving_dist):
                    stone_cur_row += moving_dist[0]
                    stone_cur_col += moving_dist[1]
                    king_cur_row = next_king_row
                    king_cur_col = next_king_col
            else:
                king_cur_row = next_king_row
                king_cur_col = next_king_col

    print(convert_pos([king_cur_col, king_cur_row], 'NUM_TO_CHAR'))
    print(convert_pos([stone_cur_col, stone_cur_row], 'NUM_TO_CHAR'))

if __name__ == '__main__':
    main()