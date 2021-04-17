from sys import stdin
from heapq import heappush, heappop

moving_dir = [[0, 1], [1, 0]]

stdin = open("./input.txt", "r")
n = int(stdin.readline())

array = [[0] * (n + 1)]
for _ in range(n):
    array.append([0] + list(map(int, stdin.readline().split())))
dist = [[float("INF")] * (n + 1) for _ in range(n + 1)]
visited = [[False] * (n + 1) for _ in range(n + 1)]


def dijkstra():
    heap = []
    heappush(heap, (0, 1, 1))
    dist[1][1] = 0
    visited[1][1] = True

    while heap:
        cur_dist, cur_row, cur_col = heappop(heap)

        if cur_dist > dist[cur_row][cur_col]:
            continue

        for moving_row, moving_col in moving_dir:
            next_row = cur_row + moving_row
            next_col = cur_col + moving_col
            if 1 <= next_row <= n and 1 <= next_col <= n:
                if not visited[next_row][next_col]:
                    if array[cur_row][cur_col] > array[next_row][next_col] and cur_dist < dist[next_row][next_col]:
                        dist[next_row][next_col] = cur_dist
                        heappush(heap, (dist[next_row][next_col], next_row, next_col))
                    else:
                        count = array[next_row][next_col] - array[cur_row][cur_col] + 1
                        if cur_dist + count < dist[next_row][next_col]:
                            dist[next_row][next_col] = cur_dist + count
                            heappush(heap, (dist[next_row][next_col], next_row, next_col))
                    visited[next_row][next_col] = True
    return dist


def main():
    dijkstra()
    print(dist[n][n])


if __name__ == '__main__':
    main()