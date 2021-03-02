from sys import stdin
from heapq import heappop, heappush

moving_dir = [[0, 1], [1, 0], [1, 1]]


# def dijkstra():
#     pq = []
#     dist = [[float("inf")] * cols for _ in range(rows)]
#     dist[0][0] = -maze[0][0]
#
#     heappush(pq, [dist[0][0], 0, 0])
#
#     while len(pq) != 0:
#         cur_dist, cur_row, cur_col = heappop(pq)
#
#         if dist[cur_row][cur_col] < cur_dist:
#             continue
#
#         for moving_row, moving_col in moving_dir:
#             next_row = cur_row + moving_row
#             next_col = cur_col + moving_col
#             if 0 <= next_row < rows and 0 <= next_col < cols:
#                 if dist[next_row][next_col] > cur_dist - maze[next_row][next_col]:
#                     dist[next_row][next_col] = cur_dist - maze[next_row][next_col]
#                     heappush(pq, [dist[next_row][next_col], next_row, next_col])
#
#     return -dist[rows - 1][cols - 1]


def main():
    stdin = open("./input.txt", "r")
    rows, cols = map(int, stdin.readline().split())

    maze = []
    for _ in range(rows):
        maze.append(list(map(int, stdin.readline().split())))

    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = maze[0][0]

    for row in range(rows):
        for col in range(cols):
            for moving_row, moving_col in moving_dir:
                next_row = row + moving_row
                next_col = col + moving_col
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    dp[next_row][next_col] = max(dp[next_row][next_col], maze[next_row][next_col] + dp[row][col])

    print(dp[rows - 1][cols - 1])

    # 시간초과
    # dijkstra
    # stdin = open("./input.txt", "r")
    # global rows, cols, maze
    #
    # rows, cols = map(int, stdin.readline().split())
    # maze = []
    # for _ in range(rows):
    #     maze.append(list(map(int, stdin.readline().split())))
    # print(dijkstra())


if __name__ == '__main__':
    main()