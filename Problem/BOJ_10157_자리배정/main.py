from sys import stdin

def main():
    cols, rows = map(int, stdin.readline().split())
    seat = int(stdin.readline().rstrip())
    stage_edge = cols * 2 + (rows - 2) * 2
    stage = [[0] * (cols + 1) for _ in range(rows + 1)]

    for y in range(rows, 0, -1):
        for x in range(1, cols + 1):
            if y == 1:
                stage[y][x] = rows + (x - 1)
            elif x == 1:
                stage[y][x] = (rows + 1) - y
            else:
                stage[y][x] = stage[y][1] + stage_edge - (x - 1)

    print(stage)

if __name__ == '__main__':
    main()