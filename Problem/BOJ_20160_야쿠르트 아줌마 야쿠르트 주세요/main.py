from sys import stdin
from heapq import heappush, heappop


def dijkstra(stores, start_store, num_of_stores):
    dist = [float('inf')] * (num_of_stores + 1)
    pq = []

    dist[start_store] = 0
    heappush(pq, (0, start_store))

    while len(pq) != 0:
        cur_dist, cur_store = heappop(pq)

        if cur_dist > dist[cur_store]:
            continue
        for next_dist, next_store in stores[cur_store]:
            if cur_dist + next_dist < dist[next_store]:
                dist[next_store] = cur_dist + next_dist
                heappush(pq, (dist[next_store], next_store))

    return dist


def main():
    stdin = open('./input.txt', 'r')
    num_of_vertexes, num_of_roads = map(int, stdin.readline().split())

    stores = {}
    for store in range(1, num_of_vertexes + 1):
        stores[store] = []

    for _ in range(num_of_roads):
        start_store, finish_store, distance = map(int, stdin.readline().split())
        stores[start_store].append((distance, finish_store))
        stores[finish_store].append((distance, start_store))

    seller_moving = list(map(int, stdin.readline().split()))
    seller_stop_by = set(seller_moving)

    my_start_store = int(stdin.readline())

    dist = {}
    for stop_by_store in seller_stop_by:
        dist[stop_by_store] = dijkstra(stores, stop_by_store, num_of_vertexes)

    answer = []
    acc_sum_of_time = [0] * len(seller_moving)
    my_dist = dijkstra(stores, my_start_store, num_of_vertexes)

    for idx, (start, finish) in enumerate(zip(seller_moving, seller_moving[1:])):
        acc_sum_of_time[idx + 1] = acc_sum_of_time[idx] + dist[start][finish]
        if acc_sum_of_time[idx + 1] != float('inf') and my_dist[finish] != float('inf'):
            if acc_sum_of_time[idx + 1] >= my_dist[finish]:
                answer.append(finish)
    print(-1 if len(answer) == 0 else min(answer))


if __name__ == '__main__':
    main()