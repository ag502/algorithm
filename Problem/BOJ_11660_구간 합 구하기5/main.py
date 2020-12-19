from sys import stdin

def get_acc_sum(array, start_row, start_col, end_row, end_col):
    acc_sum = 0
    for row in range(start_row, end_row + 1):
        if start_col == 0:
            acc_sum += array[row][end_col]
        else:
            acc_sum += array[row][end_col] - array[row][start_col - 1]

    return acc_sum

def main():
    stdin = open('./input.txt', 'r')
    n, num_of_case = map(int, stdin.readline().split())

    array = []
    acc_array = []
    for row_idx in range(n):
        row = list(map(int, stdin.readline().split()))
        acc_row = []
        for idx, num in enumerate(row):
            if idx == 0:
                acc_row.append(num)
            else:
                acc_row.append(acc_row[idx - 1] + num)

        array.append(row)
        acc_array.append(acc_row)

    for _ in range(num_of_case):
        i, j, x, y = map(int, stdin.readline().split())
        acc_sum = get_acc_sum(acc_array, i - 1, j - 1, x - 1, y - 1)
        print(acc_sum)

if __name__ == '__main__':
    main()