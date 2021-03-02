from sys import stdin
from heapq import heappush, heappop


moving_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dijkstra():
    pq = []
    visited = [[False] * cave_size for _ in range(cave_size)]
    dist = [[float("inf")] * cave_size for _ in range(cave_size)]
    dist[0][0] = cave[0][0]

    heappush(pq, [dist[0][0], 0, 0])
    visited[0][0] = True

    while len(pq) != 0:
        cur_dist, cur_row, cur_col = heappop(pq)

        if dist[cur_row][cur_col] < cur_dist:
            continue

        for moving_row, moving_col in moving_dir:
            next_row = cur_row + moving_row
            next_col = cur_col + moving_col
            if 0 <= next_row < cave_size and 0 <= next_col < cave_size and not visited[next_row][next_col]:
                if dist[next_row][next_col] > cur_dist + cave[next_row][next_col]:
                    dist[next_row][next_col] = cur_dist + cave[next_row][next_col]
                    heappush(pq, [dist[next_row][next_col], next_row, next_col])

    return dist[cave_size - 1][cave_size - 1]


def main():
    stdin = open("./input.txt", "r")
    global cave, cave_size

    phase = 0
    while True:
        phase += 1
        cave_size = int(stdin.readline().rstrip())

        if cave_size == 0:
            break

        cave = []
        for _ in range(cave_size):
            cave.append(list(map(int, stdin.readline().split())))

        print("Problem {}: {}".format(phase, dijkstra()))


if __name__ == '__main__':
    main()