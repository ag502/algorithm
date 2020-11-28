from sys import stdin
from heapq import heappush, heappop

def dijkstra(graph, start_vertex, num_of_vertexes):
    dist = [float('inf')] * (num_of_vertexes + 1)
    heap = []

    dist[start_vertex] = 0
    heappush(heap, [0, start_vertex])

    while len(heap) != 0:
        cur_dist, cur_vertex = heappop(heap)

        if dist[cur_vertex] < cur_dist:
            continue

        for next_vertex_info in graph[cur_vertex]:
            next_vertex, next_dist = next_vertex_info['next_vertex'], next_vertex_info['next_dist']
            if dist[next_vertex] > next_dist + cur_dist:
                dist[next_vertex] = next_dist + cur_dist
                heappush(heap, [next_dist + cur_dist, next_vertex])

    return dist

def main():
    stdin = open('./input.txt', 'r')
    num_of_vertexes, num_of_edges, pos_of_friend = map(int, stdin.readline().split())

    korea_map = {}
    for vertex in range(1, num_of_vertexes + 1):
        korea_map[vertex] = []

    for _ in range(num_of_edges):
        vertex_1, vertex_2, distance = map(int, stdin.readline().split())
        korea_map[vertex_1].append({'next_vertex': vertex_2, 'next_dist': distance})
        korea_map[vertex_2].append({'next_vertex': vertex_1, 'next_dist': distance})

    dist_from_start = dijkstra(korea_map, 1, num_of_vertexes)
    dist_from_friend_pos = dijkstra(korea_map, pos_of_friend, num_of_vertexes)

    start_to_friend = dist_from_start[pos_of_friend]
    friend_to_home = dist_from_friend_pos[num_of_vertexes]
    start_to_home = dist_from_start[num_of_vertexes]

    if start_to_friend + friend_to_home <= start_to_home:
        print('SAVE HIM')
    else:
        print('GOOD BYE')

if __name__ == '__main__':
    main()