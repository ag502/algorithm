from sys import stdin

moving_dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def main():
    stdin = open('./test_case.txt', 'r')
    cols, rows = map(int, stdin.readline().split())
    waiting_num = int(stdin.readline())
    seats = [[0] * cols for _ in range(rows)]

    if waiting_num > cols * rows:
        print(0)
        return

    current_row = rows - 1
    current_col = 0
    seats[current_row][current_col] = 1

    if waiting_num == 1:
        print(str(current_col + 1) + ' ' + str(rows - current_row))
        return

    number = 2
    count = 0
    for i in range(rows * cols):
        temp_row = current_row + moving_dir[count % 4][0]
        temp_col = current_col + moving_dir[count % 4][1]
        if 0 <= temp_row < rows and 0 <= temp_col < cols:
            if seats[temp_row][temp_col] == 0:
                current_row = temp_row
                current_col = temp_col
            else:
                count += 1
                current_row += moving_dir[count % 4][0]
                current_col += moving_dir[count % 4][1]
        else:
            count += 1
            current_row += moving_dir[count % 4][0]
            current_col += moving_dir[count % 4][1]
        if waiting_num == number:
            print(str(current_col + 1) + ' ' + str(rows - current_row))
            return
        seats[current_row][current_col] = number
        number += 1

if __name__ == '__main__':
    main()