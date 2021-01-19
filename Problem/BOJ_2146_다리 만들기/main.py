from sys import stdin, maxsize, setrecursionlimit
from collections import deque

setrecursionlimit(10 ** 5)

moving_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(country_map, map_size, covert_num, cur_row, cur_col):
    country_map[cur_row][cur_col] = covert_num

    for moving_row, moving_col in moving_dir:
        next_row = cur_row + moving_row
        next_col = cur_col + moving_col
        if 0 <= next_row < map_size and 0 <= next_col < map_size:
            if country_map[next_row][next_col] == 1:
                dfs(country_map, map_size, covert_num, next_row, next_col)


def bfs(country_map, map_size, visited, cur_row, cur_col):
    queue = deque()
    cur_island = country_map[cur_row][cur_col]
    visited[cur_row][cur_col] = True

    queue.append([cur_row, cur_col])

    distance = -1
    while len(queue) != 0:
        size = len(queue)

        for _ in range(size):
            cur_row, cur_col = queue.popleft()

            if country_map[cur_row][cur_col] != 0 and country_map[cur_row][cur_col] != cur_island:
                return distance

            for moving_row, moving_col in moving_dir:
                next_row = cur_row + moving_row
                next_col = cur_col + moving_col

                if 0 <= next_row < map_size and 0 <= next_col < map_size:
                    if not visited[next_row][next_col] and country_map[next_row][next_col] != cur_island:
                        queue.append([next_row, next_col])
                        # print(next_row, next_col)
                        visited[next_row][next_col] = True
        distance += 1

    return -1


def main():
    stdin = open('./input.txt', 'r')
    length_of_map = int(stdin.readline())

    county_map = []
    for _ in range(length_of_map):
        row = list(map(int, stdin.readline().split()))
        county_map.append(row)

    num_of_area = 0
    for row in range(length_of_map):
        for col in range(length_of_map):
            if county_map[row][col] == 1:
                dfs(county_map, length_of_map, num_of_area + 2, row, col)
                num_of_area += 1

    # print(num_of_area)
    # for row in range(length_of_map):
    #     print(county_map[row])

    answer = maxsize
    for row in range(length_of_map):
        for col in range(length_of_map):
            visited = [[False] * length_of_map for _ in range(length_of_map)]
            if county_map[row][col] != 0:
                distance = bfs(county_map, length_of_map, visited, row, col)
                if distance != -1:
                    answer = min(answer, distance)

    print(answer)


if __name__ == '__main__':
    main()