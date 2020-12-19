from sys import stdin

def get_acc_sum(array, start_row, start_col, end_row, end_col):
    acc_sum = 0
    for row in  range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            acc_sum += array[row][col]
    return acc_sum

def main():
    stdin = open('./input.txt', 'r')
    rows, cols = map(int, stdin.readline().split())
    array = []

    for _ in range(rows):
        array.append(list(map(int, stdin.readline().split())))

    num_of_case = int(stdin.readline())
    for _ in range(num_of_case):
        i, j, x, y = map(int, stdin.readline().split())
        acc_sum = get_acc_sum(array, i -1 , j - 1, x - 1, y - 1)
        print(acc_sum)

if __name__ == '__main__':
    main()