from sys import stdin

moving_dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def main():
    stdin = open("./input.txt", "r")
    rows, cols, rotation_count = map(int, stdin.readline().split())

    array = []
    for _ in range(rows):
        array.append(list(map(int, stdin.readline().split())))

    for _ in range(rotation_count):
        for i in range(min(rows, cols) // 2):
            cur_rows = rows - (i * 2)
            cur_cols = cols - (i * 2)

            cur_row = i
            cur_col = i
            start_value = array[cur_row][cur_col]
            temp = start_value
            temp2 = start_value

            idx = 0
            while idx < 4:
                cur_row = cur_row + moving_dir[idx][0]
                cur_col = cur_col + moving_dir[idx][1]

                if i <= cur_row < i + cur_rows and i <= cur_col < i + cur_cols:
                    temp2 = array[cur_row][cur_col]
                    array[cur_row][cur_col] = temp
                    temp = temp2
                else:
                    cur_row -= moving_dir[idx][0]
                    cur_col -= moving_dir[idx][1]
                    idx += 1

    for row in array:
        print(' '.join(list(map(str, row))))


if __name__ == '__main__':
    main()