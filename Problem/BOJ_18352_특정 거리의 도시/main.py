from sys import stdin
from heapq import heappush, heappop

MAX = 300000

def main():
    N, M, K, X = map(int, stdin.readline().split())
    city_map = {}
    dist = [MAX + 1] * (N + 1)

    for city in range(1, N + 1):
        city_map[city] = []
    for road in range(1, M + 1):
        city1, city2 = map(int, stdin.readline().split())
        city_map[city1].append(city2)

    priority_queue = []
    dist[X] = 0
    heappush(priority_queue, [0, X])

    while len(priority_queue) != 0:
        distance, start_city = heappop(priority_queue)

        # 해당 도시의 최단 거리가 기존의 알려져 있던 최단 거리보다 크다면 무시
        if distance > dist[start_city]:
            continue

        # 인접 도시 순회
        for next_city in city_map[start_city]:
            distance = dist[start_city] + 1
            if distance < dist[next_city]:
                dist[next_city] = distance
                heappush(priority_queue, [distance, next_city])

    answer = []
    for idx, distance in enumerate(dist):
        if distance == K:
            answer.append(idx)

    if len(answer) == 0:
        print(-1)
    else:
        for city in answer:
            print(city)

if __name__ == '__main__':
    main()