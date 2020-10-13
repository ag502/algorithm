from sys import stdin
from collections import deque

def main():
    n, e = map(int, stdin.readline().split())
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []

    for _ in range(e):
        a, b, c = map(int, stdin.readline().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    stop_by_1, stop_by_2 = map(int, stdin.readline().split())

    dist_0 = dijkstra(1, graph, n)
    dist_1 = dijkstra(stop_by_1, graph, n)
    dist_2 = dijkstra(stop_by_2, graph, n)

    # print(dist_0, dist_1, dist_2)

    answer = min(dist_0[stop_by_1] + dist_1[stop_by_2] + dist_2[n],
                 dist_0[stop_by_2] + dist_2[stop_by_1] + dist_1[n])

    print(answer if answer != float('inf') else -1)

def dijkstra(start_vertex, graph, n):
    dist = [float('inf')] * (n + 1)
    pq = deque()

    dist[start_vertex] = 0
    pq.append([start_vertex, 0])

    while len(pq) != 0:
        cur_vertex, cur_distance = pq.popleft()

        if cur_distance > dist[cur_vertex]:
            continue

        for next_vertex, next_distance in graph[cur_vertex]:
            if dist[next_vertex] > dist[cur_vertex] + next_distance:
                dist[next_vertex] = dist[cur_vertex] + next_distance
                pq.append([next_vertex, dist[next_vertex]])

    return dist

if __name__ == '__main__':
    main()