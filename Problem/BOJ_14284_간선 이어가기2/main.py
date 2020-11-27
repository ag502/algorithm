from sys import stdin
from heapq import heappush, heappop

def dijkstra(graph, num_of_vertexes, start_vertex):
    heap = []
    dist = [float('inf')] * (num_of_vertexes + 1)

    dist[start_vertex] = 0
    heappush(heap, [0, start_vertex])

    while len(heap) != 0:
        cur_dist, cur_vertex = heappop(heap)
        if dist[cur_vertex] < cur_dist:
            continue

        for next_vertex, next_dist in graph[cur_vertex]:
            if dist[next_vertex] > cur_dist + next_dist:
                dist[next_vertex] = cur_dist + next_dist
                heappush(heap, [cur_dist + next_dist, next_vertex])

    return dist

def main():
    stdin = open('./input.txt', 'r')
    num_of_vertexes, num_of_path = map(int, stdin.readline().split())

    graph = {}
    for vertex in range(1, num_of_vertexes + 1):
        graph[vertex] = []

    for _ in range(num_of_path):
        vertex_1, vertex_2, weight = map(int, stdin.readline().split())
        graph[vertex_1].append([vertex_2, weight])
        graph[vertex_2].append([vertex_1, weight])

    start_vertex, finish_vertex = map(int, stdin.readline().split())
    dist = dijkstra(graph, num_of_vertexes, start_vertex)

    print(dist[finish_vertex])

if __name__ == '__main__':
    main()