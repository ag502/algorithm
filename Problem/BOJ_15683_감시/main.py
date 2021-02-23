from sys import stdin


def rotate(camera_type, cur_row, cur_col):
    areas = [0, 0, 0, 0]

    for row in range(cur_row - 1, -1, -1):
        if office[row][cur_col] == '6':
            break
        elif office[row][cur_col] == '0' or office[row][cur_col] == "#":
            areas[0] += 1

    for col in range(cur_col + 1, cols):
        if office[cur_row][col] == '6':
            break
        elif office[cur_row][col] == '0' or office[cur_row][col] == "#":
            areas[1] += 1

    for row in range(cur_row + 1, rows):
        if office[row][cur_col] == '6':
            break
        elif office[row][cur_col] == '0' or office[row][cur_col] == "#":
            areas[2] += 1

    for col in range(cur_col - 1, -1, -1):
        if office[cur_row][col] == '6':
            break
        elif office[cur_row][col] == '0' or office[cur_row][col] == "#":
            areas[3] += 1

    print(areas)
    direction = ''
    if camera_type == '1':
        temp = 0
        for idx, area in enumerate(areas):
            if temp < area:
                temp = area
                if idx == 0:
                    direction = 'N'
                elif idx == 1:
                    direction = 'E'
                elif idx == 2:
                    direction = 'S'
                else:
                    direction = 'W'
    elif camera_type == '2':
        if areas[0] + areas[2] < areas[1] + areas[3]:
            direction = 'WE'
        else:
            direction = 'NS'
    elif camera_type == '3':
        comb_areas = [areas[0] + areas[1], areas[1] + areas[2], areas[2] + areas[3], areas[3] + areas[0]]
        temp = 0
        for idx, comb_area in enumerate(comb_areas):
            if temp < comb_area:
                temp = comb_area
                if idx == 0:
                    direction = 'NE'
                elif idx == 1:
                    direction = 'ES'
                elif idx == 2:
                    direction = 'WS'
                else:
                    direction = 'WN'
    elif camera_type == '4':
        comb_areas = [
            areas[3] + areas[0] + areas[1],
            areas[0] + areas[1] + areas[2],
            areas[1] + areas[2] + areas[3],
            areas[2] + areas[3] + areas[0]
        ]
        temp = 0
        for idx, comb_area in enumerate(comb_areas):
            if temp < comb_area:
                temp = comb_area
                if idx == 0:
                    direction = 'WNE'
                elif idx == 1:
                    direction = 'NES'
                elif idx == 2:
                    direction = 'ESW'
                else:
                    direction = 'SWN'
    else:
        direction = 'NESW'
    return direction


def mark(direction, cur_row, cur_col):
    if direction == 'N':
        for row in range(cur_row - 1, -1, -1):
            if office[row][cur_col] == '6':
                break
            elif office[row][cur_col] == '0':
                office[row][cur_col] = '#'
    elif direction == 'E':
        for col in range(cur_col + 1, cols):
            if office[cur_row][col] == '6':
                break
            elif office[cur_row][col] == '0':
                office[cur_row][col] = '#'
    elif direction == 'S':
        for row in range(cur_row + 1, rows):
            if office[row][cur_col] == '6':
                break
            elif office[row][cur_col] == '0':
                office[row][cur_col] = '#'
    elif direction == 'W':
        for col in range(cur_col - 1, -1, -1):
            if office[cur_row][col] == '6':
                break
            elif office[cur_row][col] == '0':
                office[cur_row][col] = '#'


def mark_office(camera_type, cur_row, cur_col):
    direction = rotate(camera_type, cur_row, cur_col)
    print(direction)
    for way in direction:
        mark(way, cur_row, cur_col)


def main():
    stdin = open("./input.txt", "r")
    global rows, cols, office

    rows, cols = map(int, stdin.readline().split())
    office = []

    for _ in range(rows):
        office.append(stdin.readline().split())

    for row in range(rows):
        for col in range(cols):
            if office[row][col] in ['1', '2', '3', '4', '5']:
                mark_office(office[row][col], row, col)

    for row in office:
        print(row)


if __name__ == '__main__':
    main()