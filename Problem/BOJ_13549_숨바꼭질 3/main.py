from sys import stdin
from heapq import heappush, heappop

def main():
    start_position, finish_position = map(int, stdin.readline().split())
    dist = [float('inf')] * 100001
    pq = []

    heappush(pq, [0, start_position])
    dist[start_position] = 0

    while len(pq) != 0:
        distance, cur_position = heappop(pq)

        if cur_position == finish_position:
            print(dist[cur_position])
            break

        if distance > dist[cur_position]:
            continue

        # 갈 수 있는 위치 탐색
        if 0 <= cur_position + 1 <= 100000:
            if dist[cur_position + 1] > distance + 1:
                dist[cur_position + 1] = distance + 1
                heappush(pq, [distance + 1, cur_position + 1])
        if 0 <= cur_position - 1 <= 100000:
            if dist[cur_position - 1] > distance + 1:
                dist[cur_position - 1] = distance + 1
                heappush(pq, [distance + 1, cur_position - 1])
        if 0 <= cur_position * 2 <= 100000:
            if dist[cur_position * 2] > distance:
                dist[cur_position * 2] = distance
                heappush(pq, [distance, cur_position * 2])


if __name__ == '__main__':
    main()
