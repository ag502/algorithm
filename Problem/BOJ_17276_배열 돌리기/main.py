from sys import stdin

clock_way = [[0, 1], [1, 0], [0, -1], [-1, 0]]
anti_clock_way = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def main():
    stdin = open("./input.txt", "r")
    test_case = int(stdin.readline())

    for _ in range(test_case):
        n, degree = map(int, stdin.readline().split())
        array = []
        for _ in range(n):
            array.append(list(map(int, stdin.readline().split())))
        for _ in range(abs(degree // 45)):
            for i in range(n // 2):
                cur_row = i
                cur_col = i
                cur_rows = n - (i * 2)
                cur_cols = n - (i * 2)
                start_value = array[cur_row][cur_col]
                idx = 0
                while idx < 4:
                    # print(idx)
                    if degree < 0:
                        cur_row += ((n // 2) - i) * anti_clock_way[idx][0]
                        cur_col += ((n // 2) - i) * anti_clock_way[idx][1]
                    else:
                        cur_row += ((n // 2) - i) * clock_way[idx][0]
                        cur_col += ((n // 2) - i) * clock_way[idx][1]

                    # print(cur_row, cur_col)
                    if i <= cur_row < i + cur_rows and i <= cur_col < i + cur_cols:
                        # print(start_value)
                        temp = array[cur_row][cur_col]
                        array[cur_row][cur_col] = start_value
                        start_value = temp
                    else:
                        if degree < 0:
                            cur_row -= ((n // 2) - i) * anti_clock_way[idx][0]
                            cur_col -= ((n // 2) - i) * anti_clock_way[idx][1]
                        else:
                            cur_row -= ((n // 2) - i) * clock_way[idx][0]
                            cur_col -= ((n // 2) - i) * clock_way[idx][1]
                        idx += 1

        for row in array:
            print(' '.join(list(map(str, row))))


if __name__ == '__main__':
    main()