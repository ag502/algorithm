from sys import stdin
from heapq import heappush, heappop

moving_dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def main():
    stdin = open('./test_case.txt', 'r')
    cols, rows = map(int, stdin.readline().split())
    maze = []
    dist = [[float('inf')] * cols for _ in range(rows)]
    pq = []

    for _ in range(rows):
        row = list(stdin.readline().rstrip())
        maze.append(row)

    dist[0][0] = 0
    maze[0][0] = '-1'
    heappush(pq, [0, 0, 0])

    while len(pq) != 0:
        cur_dist, cur_row, cur_col = heappop(pq)

        if dist[cur_row][cur_col] < cur_dist:
            continue

        for moving_row, moving_col in moving_dir:
            next_row = cur_row + moving_row
            next_col = cur_col + moving_col
            if 0 <= next_row < rows and 0 <= next_col < cols:
                if maze[next_row][next_col] != '-1':
                    dist[next_row][next_col] = min(dist[next_row][next_col], int(maze[next_row][next_col]) + cur_dist)
                    heappush(pq, [dist[next_row][next_col], next_row, next_col])
                    maze[next_row][next_col] = '-1'

    print(dist[rows - 1][cols - 1])

if __name__ == '__main__':
    main()