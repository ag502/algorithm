from sys import stdin
from heapq import heappush, heappop


def dijkstra(villages, start_home):
    dist = [float('inf')] * (len(villages) + 1)
    heap = []

    dist[start_home] = 0
    heappush(heap, (0, start_home))

    while len(heap) != 0:
        cur_dist, cur_home = heappop(heap)

        if dist[cur_home] < cur_dist:
            continue
        for next_home, next_dist in villages[cur_home]:
            if cur_dist + next_dist < dist[next_home]:
                dist[next_home] = cur_dist + next_dist
                heappush(heap, (dist[next_home], next_home))
    return dist


def main():
    stdin = open('./input.txt', 'r')
    num_of_homes, num_of_roads, destination = map(int, stdin.readline().split())

    villages = {}
    for village in range(1, num_of_homes + 1):
        villages[village] = []

    for _ in range(num_of_roads):
        start_home, end_home, time = map(int, stdin.readline().split())
        villages[start_home].append((end_home, time))

    # print(villages)

    dist_home_to_dest = [0] * (num_of_homes + 1)
    dist_dest_to_home = dijkstra(villages, destination)

    for home in range(1, num_of_homes + 1):
        dist_home_to_dest[home] = dijkstra(villages, home)[destination]

    answer = 0
    for d1, d2 in zip(dist_home_to_dest[1:], dist_dest_to_home[1:]):
        answer = max(answer, d1 + d2)

    print(answer)


if __name__ == '__main__':
    main()
