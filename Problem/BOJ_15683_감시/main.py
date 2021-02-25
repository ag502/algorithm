from sys import stdin, maxsize
from copy import deepcopy


stdin = open("./input.txt", "r")
rows, cols = map(int, stdin.readline().split())

camera_info = []
office = []

for _ in range(rows):
    office.append(stdin.readline().rstrip().split())
# temp_office = deepcopy(office)
answer = [maxsize]


def array_copy(array1, array2):
    for row in range(rows):
        for col in range(cols):
            array1[row][col] = array2[row][col]


def rotate(direction, cur_row, cur_col):
    if direction == 0:
        for row in range(cur_row, -1, -1):
            if office[row][cur_col] == "6":
                break
            if office[row][cur_col] == "0":
                office[row][cur_col] = "#"
    elif direction == 1:
        for col in range(cur_col, cols):
            if office[cur_row][col] == "6":
                break
            if office[cur_row][col] == "0":
                office[cur_row][col] = "#"
    elif direction == 2:
        for row in range(cur_row, rows):
            if office[row][cur_col] == "6":
                break
            if office[row][cur_col] == "0":
                office[row][cur_col] = "#"
    elif direction == 3:
        for col in range(cur_col, -1, -1):
            if office[cur_row][col] == "6":
                break
            if office[cur_row][col] == "0":
                office[cur_row][col] = "#"


def dfs(idx):

    if idx >= len(camera_info):
        # for row in office:
        #     print(row)
        # print("---------------------")
        count = 0
        for row in range(rows):
            for col in range(cols):
                if office[row][col] == "0":
                    count += 1
        answer[0] = min(answer[0], count)
        return

    temp_office = [['0'] * cols for _ in range(rows)]
    array_copy(temp_office, office)

    # if idx < len(camera_info):
    camera_type, cur_row, cur_col = camera_info[idx]
    if camera_type == "1":
        for direction in range(4):
            rotate(direction, cur_row, cur_col)
            dfs(idx + 1)
            array_copy(office, temp_office)
    elif camera_type == "2":
        for direction in range(2):
            rotate(direction, cur_row, cur_col)
            rotate(direction + 2, cur_row, cur_col)
            dfs(idx + 1)
            array_copy(office, temp_office)
    elif camera_type == "3":
        for direction in range(4):
            rotate(direction, cur_row, cur_col)
            rotate((direction + 1) % 4, cur_row, cur_col)
            dfs(idx + 1)
            array_copy(office, temp_office)
    elif camera_type == "4":
        for direction in range(4):
            rotate(direction, cur_row, cur_col)
            rotate((direction + 1) % 4, cur_row, cur_col)
            rotate((direction + 2) % 4, cur_row, cur_col)
            dfs(idx + 1)
            array_copy(office, temp_office)
    else:
        for direction in range(4):
            rotate(direction, cur_row, cur_col)
        dfs(idx + 1)
        array_copy(office, temp_office)

    # array_copy(office, temp_office)


def main():
    for row in range(rows):
        for col in range(cols):
            if office[row][col] != "6" and office[row][col] != "0":
                camera_info.append([office[row][col], row, col])

    # print(camera_info)
    dfs(0)

    print(answer[0])


if __name__ == '__main__':
    main()