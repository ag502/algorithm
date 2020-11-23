from sys import stdin
from heapq import heappush, heappop

moving_dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def main():
    stdin = open('./input.txt', 'r')
    width = int(stdin.readline())
    rooms = []
    heap = []
    dist = [[float('inf')] * width for _ in range(width)]


    for _ in range(width):
        rows = list(map(int, list(stdin.readline().rstrip())))
        rooms.append(rows)

    dist[0][0] = 0
    rooms[0][0] = -2
    heappush(heap, [0, 0, 0])

    while len(heap) != 0:
        cur_dist, cur_row, cur_col = heappop(heap)

        if cur_dist > dist[cur_row][cur_col]:
            continue

        for moving_row, moving_col in moving_dir:
            next_row = cur_row + moving_row
            next_col = cur_col + moving_col
            if 0 <= next_row < width and 0 <= next_col < width and rooms[next_row][next_col] != -2:
                if rooms[next_row][next_col] == 0:
                    dist[next_row][next_col] = min(dist[next_row][next_col], cur_dist + 1)
                elif rooms[next_row][next_col] == 1:
                    dist[next_row][next_col] = min(dist[next_row][next_col], cur_dist)
                rooms[next_row][next_col] = -2
                heappush(heap, [dist[next_row][next_col], next_row, next_col])

    print(dist[width - 1][width - 1])

if __name__ == '__main__':
    main()