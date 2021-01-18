from sys import stdin
from collections import deque

moving_dir = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]


def bfs(building, floors, rows, cols, cur_row, cur_col, cur_floor):
    queue = deque()
    building[cur_floor][cur_row][cur_col] = "-"
    queue.append([cur_row, cur_col, cur_floor])

    distance = 0
    while len(queue) != 0:
        size = len(queue)
        for _ in range(size):
            cur_row, cur_col, cur_floor = queue.popleft()

            if building[cur_floor][cur_row][cur_col] == 'E':
                return distance

            for moving_row, moving_col, moving_floor in moving_dir:
                next_row = cur_row + moving_row
                next_col = cur_col + moving_col
                next_floor = cur_floor + moving_floor
                if 0 <= next_row < rows and 0 <= next_col < cols and 0 <= next_floor < floors:
                    if building[next_floor][next_row][next_col] == '.' or \
                            building[next_floor][next_row][next_col] == 'E':
                        if building[next_floor][next_row][next_col] != 'E':
                            building[next_floor][next_row][next_col] = '_'
                        queue.append([next_row, next_col, next_floor])
        distance += 1

    return -1


def main():
    stdin = open('./input.txt', 'r')

    while True:
        num_of_floors, rows, cols = map(int, stdin.readline().split())

        if num_of_floors == 0 and rows == 0 and cols == 0:
            break

        building = []
        for _ in range(num_of_floors):
            floor = []
            for _ in range(rows + 1):
                row = list(stdin.readline().rstrip())
                if len(row) != 0:
                    floor.append(row)
            building.append(floor)

        start_point = []
        for floor in range(num_of_floors):
            for row in range(rows):
                for col in range(cols):
                    if building[floor][row][col] == 'S':
                        start_point.append(row)
                        start_point.append(col)
                        start_point.append(floor)
                        break

        distance = bfs(building, num_of_floors, rows, cols, start_point[0], start_point[1], start_point[2])

        if distance == -1:
            print("Trapped!")
        else:
            print(f"Escaped in {distance} minute(s).")


if __name__ == '__main__':
    main()
