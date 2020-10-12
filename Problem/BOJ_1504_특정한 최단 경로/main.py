from sys import stdin
from collections import deque

def main():
    n, e = map(int, stdin.readline().split())
    # graph = {}
    # for i in range(1, n + 1):
    #     graph[i] = []
    #
    # dist = [float('INF')] * (n + 1)
    # pq = deque()
    #
    # for _ in range(e):
    #     a, b, c = map(int, stdin.readline().split())
    #     graph[a].append([b, c])
    #     graph[b].append([a, c])
    #
    # # Dijkstra
    # pq.append([1, 0])
    # dist[1] = 0
    #
    # while len(pq) != 0:
    #     cur_vertex, cur_distance = pq.popleft()
    #
    #     if cur_distance > dist[cur_vertex]:
    #         continue
    #
    #     for next_vertex, next_distance in graph[cur_vertex]:
    #         if dist[next_vertex] > next_distance + cur_distance:
    #             dist[next_vertex] = next_distance + cur_distance
    #             pq.append([next_vertex, next_distance + cur_distance])
    #
    # print(dist)

    # Floyd-Warshall
    graph = [[float('INF')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0

    for _ in range(e):
        a, b, c = map(int, stdin.readline().split())
        graph[a][b] = c
        graph[b][a] = c

    stop_by = list(map(int, stdin.readline().split()))

    for k in stop_by:
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    print(graph)
    answer = min(graph[1][stop_by[0]] + graph[stop_by[0]][stop_by[1]] + graph[stop_by[1]][n],
                 graph[1][stop_by[1]] + graph[stop_by[0]][stop_by[1]] + graph[stop_by[0]][n])
    print(answer if answer != float('INF') else -1)

if __name__ == '__main__':
    main()