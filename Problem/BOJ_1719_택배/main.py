from sys import stdin
from collections import deque
from heapq import heappush, heappop


def dijkstra(herbs, start_herb):
    pq = []
    dist = [float('inf')] * (len(herbs) + 1)
    parents = [-1] * (len(herbs) + 1)

    heappush(pq, (0, start_herb))
    dist[start_herb] = 0
    parents[start_herb] = start_herb

    while len(pq) != 0:
        cur_dist, cur_herb = heappop(pq)

        if cur_dist > dist[cur_herb]:
            continue
        for next_dist, next_herb in herbs[cur_herb]:
            if cur_dist + next_dist < dist[next_herb]:
                dist[next_herb] = cur_dist + next_dist
                heappush(pq, (dist[next_herb], next_herb))
                parents[next_herb] = cur_herb

    return dist, parents


def shortest_path(parent, start_herb, cur_herb):
    path = deque()
    while parent[cur_herb] != cur_herb:
        path.appendleft(cur_herb)
        cur_herb = parent[cur_herb]
    path.appendleft(start_herb)
    return path


def main():
    stdin = open('./input.txt', 'r')
    num_of_herbs, num_of_paths = map(int, stdin.readline().split())

    herbs = {}
    for i in range(1, num_of_herbs + 1):
        herbs[i] = []

    for _ in range(num_of_paths):
        start_herb, finish_herb, time = map(int, stdin.readline().split())
        herbs[start_herb].append((time, finish_herb))
        herbs[finish_herb].append((time, start_herb))

    path_table = [["-"] * len(herbs) for _ in range(len(herbs))]

    for start_herb in herbs.keys():
        dist, parents = dijkstra(herbs, start_herb)
        print(parents)

        for end_herb, distance in enumerate(dist):
            if end_herb != 0 and distance != 0:
                path = shortest_path(parents, start_herb, end_herb)
                print(path)
                path_table[start_herb - 1][end_herb - 1] = str(path[1])

    for row in path_table:
        print(' '.join(row))


if __name__ == '__main__':
    main()