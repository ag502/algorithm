from sys import stdin
from heapq import heappush, heappop

MAX = 10000000000

def main():
    n = int(stdin.readline())
    m = int(stdin.readline())

    city_map = {}
    for i in range(1, n + 1):
        city_map[i] = []

    dist = [MAX + 1] * (n + 1)
    pq = []

    for _ in range(m):
        s, f, w = map(int, stdin.readline().split())
        city_map[s].append([f, w])

    start_city, finish_city = map(int, stdin.readline().split())

    heappush(pq, [0, start_city])
    dist[start_city] = 0

    while len(pq) != 0:
        distance, cur_city = heappop(pq)
        if distance > dist[cur_city]:
            continue

        for next_city, weight in city_map[cur_city]:
            if distance + weight < dist[next_city]:
                dist[next_city] = distance + weight
                heappush(pq, [distance + weight, next_city])

    print(dist[finish_city])
if __name__ == '__main__':
    main()