from sys import stdin
from heapq import heappush, heappop

# [row, col]
moving_dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def dijkstra(city_map, rows, cols):
    dist = [[float('inf')] * cols for _ in range(rows)]
    heap = []

    # [distance, row, col]
    heappush(heap, [city_map[0][0], 0, 0])
    dist[0][0] = city_map[0][0]
    city_map[0][0] = -2

    while len(heap) != 0:
        cur_dist, cur_row, cur_col = heappop(heap)

        if dist[cur_row][cur_col] < cur_dist:
            continue

        for moving_row, moving_col in moving_dir:
            next_row = cur_row + moving_row
            next_col = cur_col + moving_col
            if 0 <= next_row < rows and 0 <= next_col < cols:
                if city_map[next_row][next_col] != -1 and city_map[next_row][next_col] != -2:
                    if dist[next_row][next_col] > city_map[next_row][next_col] + cur_dist:
                        dist[next_row][next_col] = city_map[next_row][next_col] + cur_dist
                        heappush(heap, [dist[next_row][next_col], next_row, next_col])
                        city_map[next_row][next_col] = -2

    return dist


def main():
    stdin = open('./input.txt', 'r')
    rows, cols = map(int, stdin.readline().split())

    city_map =[]
    for _ in range(rows):
        city_map.append(list(map(int, stdin.readline().split())))

    if city_map[0][0] == -1:
        print(-1)
    else:
        dist = dijkstra(city_map, rows, cols)
        print(-1 if dist[rows - 1][cols - 1] == float('inf') else dist[rows - 1][cols - 1])

if __name__ == '__main__':
    main()