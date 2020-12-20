from sys import stdin

def get_acc_sum(array, start_row, start_col, end_row, end_col):
    acc_sum = 0
    square = array[end_row][end_col]
    subtract_square_1, subtract_square_2 = 0, 0
    common_square = 0

    if start_row != 0:
        subtract_square_1 = array[start_row - 1][end_col]
    if start_col != 0:
        subtract_square_2 = array[end_row][start_col - 1]
    if start_row != 0 and start_col != 0:
        common_square = array[start_row - 1][start_col - 1]

    acc_sum = square - subtract_square_1 - subtract_square_2 + common_square
    return acc_sum

def main():
    stdin = open('./input.txt', 'r')
    n, num_of_case = map(int, stdin.readline().split())

    array = []
    for row_idx in range(n):
        row = list(map(int, stdin.readline().split()))
        array.append(row)

    acc_array = [[0] * n for _ in range(n)]
    # 열 누적합
    for row in range(len(acc_array)):
        for col in range(len(acc_array[row])):
            if col == 0:
                acc_array[row][col] = array[row][col]
            else:
                acc_array[row][col] = acc_array[row][col - 1] + array[row][col]

    # 행 누적합
    for col in range(len(acc_array)):
        for row in range(len(acc_array[col])):
            if row == 0:
                continue
            acc_array[row][col] = acc_array[row][col] + acc_array[row - 1][col]

    for _ in range(num_of_case):
        i, j, x, y = map(int, stdin.readline().split())
        acc_sum = get_acc_sum(acc_array, i - 1, j - 1, x - 1, y - 1)
        print(acc_sum)

if __name__ == '__main__':
    main()