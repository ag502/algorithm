from sys import stdin
from heapq import heappush, heappop

def main():
    n, m = map(int, stdin.readline().split())
    road_map = {}
    dist = [float('inf')] * (n + 1)
    priority_queue = []

    for barn in range(1, n + 1):
        road_map[barn] = []

    for _ in range(m):
        barn1, barn2, cows = map(int, stdin.readline().split())
        road_map[barn1].append([barn2, cows])
        road_map[barn2].append([barn1, cows])

    # Dijkstra

    # 1. 출발지
    heappush(priority_queue, [1, 0])
    dist[1] = 0

    while len(priority_queue) != 0:
        cur_barn, distance = heappop(priority_queue)

        if distance > dist[cur_barn]:
            continue

        # 갈 수 있는 주변 헛간 탐색
        for next_barn, cows in road_map[cur_barn]:
            # 갈 수 있는 주변 헛간의 기존 소들의 마릿수 보다
            # 계산된 소들의 마릿수가 작다면
            # 계산된 소들의 값으로 갱신
            if dist[cur_barn] + cows < dist[next_barn]:
                heappush(priority_queue, [next_barn, dist[cur_barn] + cows])
                dist[next_barn] = dist[cur_barn] + cows

    print(dist[n])

if __name__ == '__main__':
    main()
