from sys import stdin
from heapq import heappush, heappop

MAX = 3000000

def main():
    v, e = map(int, stdin.readline().split())
    start_node = int(stdin.readline())
    dist = [MAX] * (v + 1)
    pq = []
    graph = {}

    for i in range(1, v + 1):
        graph[i] = []

    # {1: [[v, w], [v, w]], 2: [] .... }
    for _ in range(e):
        u, v, w = map(int, stdin.readline().split())
        graph[u].append([v, w])

    heappush(pq, [0, start_node])
    dist[start_node] = 0

    while len(pq) != 0:
        distance, cur_node = heappop(pq)
        if distance > dist[cur_node]:
            continue

        for next_node, weight in graph[cur_node]:
            if distance + weight < dist[next_node]:
                dist[next_node] = distance + weight
                heappush(pq, [distance + weight, next_node])

    for min_distance in dist[1:]:
        if min_distance >= 3000000:
            print("INF")
        else:
            print(min_distance)

if __name__ == '__main__':
    main()