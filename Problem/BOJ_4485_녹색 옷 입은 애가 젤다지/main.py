from sys import stdin
from heapq import heappush, heappop

moving_dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def bfs(cage, width):
    dist = [[float('inf')] * width for _ in range(width)]
    pq = []

    dist[0][0] = cage[0][0]
    heappush(pq, [cage[0][0], 0, 0])
    cage[0][0] = -1

    while len(pq) != 0:
        cur_dist, cur_row, cur_col = heappop(pq)

        if dist[cur_row][cur_col] < cur_dist:
            continue

        for moving_row, moving_col in moving_dir:
            next_row = cur_row + moving_row
            next_col = cur_col + moving_col
            if 0 <= next_row < width and 0 <= next_col < width:
                if cage[next_row][next_col] != -1:
                    dist[next_row][next_col] = min(dist[next_row][next_col], dist[cur_row][cur_col] + cage[next_row][next_col])
                    heappush(pq, [dist[cur_row][cur_col] + cage[next_row][next_col], next_row, next_col])
                    cage[next_row][next_col] = -1

    return dist

def main():
    stdin = open('./test_case.txt', 'r')
    answer = []
    while True:
        width = int(stdin.readline())
        cage = []

        if width == 0:
            break

        for _ in range(width):
            row = list(map(int, stdin.readline().split()))
            cage.append(row)

        dist = bfs(cage, width)
        answer.append(dist[width - 1][width - 1])

    for idx, money in enumerate(answer):
        print('Problem ' + str(idx + 1) + ': ' + str(money))

if __name__ == '__main__':
    main()