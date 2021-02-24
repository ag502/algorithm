from sys import stdin
from copy import deepcopy
from itertools import product

directions = ['N', 'S', 'E', 'W']


def mark(type, cur_row, cur_col):
    if type == 1:
        for row in range(cur_row, -1, -1):
            if temp_office[row][cur_col] == '0':
                temp_office[row][cur_col] = '#'
            elif temp_office[row][cur_col] == '6':
                break
    elif type == 2:
        for col in range(cur_col, cols):
            if temp_office[cur_row][col] == '0':
                temp_office[cur_row][col] = '#'
            elif temp_office[cur_row][col] == '6':
                break
    elif type == 3:
        for row in range(cur_row, rows):
            if temp_office[row][cur_col] == '0':
                temp_office[row][cur_col] = '#'
            elif temp_office[row][cur_col] == '6':
                break
    elif type == 4:
        for col in range(cur_col, -1, -1):
            if temp_office[cur_row][col] == '0':
                temp_office[cur_row][col] = '#'
            elif temp_office[cur_row][col] == '6':
                break


def rotate(camera_info, direction):
    camera_type, cur_row, cur_col = camera_info
    if camera_type == '1':
        if direction == 'N':
            mark(1, cur_row, cur_col)
        elif direction == 'E':
            mark(2, cur_row, cur_col)
        elif direction == 'S':
            mark(3, cur_row, cur_col)
        else:
            mark(4, cur_row, cur_col)

    elif camera_type == '2':
        if direction == 'W' or direction == 'E':
            mark(4, cur_row, cur_col)
            mark(2, cur_row, cur_col)
        else:
            mark(1, cur_row, cur_col)
            mark(3, cur_row, cur_col)

    elif camera_type == '3':
        if direction == 'N':
            mark(1, cur_row, cur_col)
            mark(2, cur_row, cur_col)
        elif direction == "E":
            mark(2, cur_row, cur_col)
            mark(3, cur_row, cur_col)

        elif direction == 'S':
            mark(3, cur_row, cur_col)
            mark(4, cur_row, cur_col)
        else:
            mark(4, cur_row, cur_col)
            mark(1, cur_row, cur_col)

    elif camera_type == '4':
        if direction == 'N':
            mark(4, cur_row, cur_col)
            mark(1, cur_row, cur_col)
            mark(2, cur_row, cur_col)
        elif direction == 'E':
            mark(1, cur_row, cur_col)
            mark(2, cur_row, cur_col)
            mark(3, cur_row, cur_col)
        elif direction == 'S':
            mark(2, cur_row, cur_col)
            mark(3, cur_row, cur_col)
            mark(4, cur_row, cur_col)
        else:
            mark(3, cur_row, cur_col)
            mark(4, cur_row, cur_col)
            mark(1, cur_row, cur_col)
    else:
        mark(1, cur_row, cur_col)
        mark(2, cur_row, cur_col)
        mark(3, cur_row, cur_col)
        mark(4, cur_row, cur_col)


def main():
    stdin = open("./input.txt", "r")
    global rows, cols, office, temp_office, cameras, visited
    rows, cols = map(int, stdin.readline().split())

    office = []
    for _ in range(rows):
        office.append(list(stdin.readline().rstrip().split()))

    # print(office)
    cameras = []
    for row in range(rows):
        for col in range(cols):
            if office[row][col] != '0' and office[row][col] != '6':
                cameras.append((office[row][col], row, col))

    comb_dir = list(product(directions, repeat=len(cameras)))

    answer = []
    for idx, direction in enumerate(comb_dir):
        temp_office = deepcopy(office)
        temp = 0
        for dir, camera_info in zip(direction, cameras):
            rotate(camera_info, dir)

        for row in range(rows):
            for col in range(cols):
                if temp_office[row][col] == '0':
                    temp += 1

        answer.append(temp)

    print(min(answer))


if __name__ == '__main__':
    main()