from sys import stdin
from heapq import heappush, heappop


def dijkstra(homes, start_home):
    dist = [float('inf')] * len(homes)
    pq = []

    dist[start_home] = 0
    heappush(pq, (0, start_home))

    while len(pq) != 0:
        cur_time, cur_home = heappop(pq)

        if cur_time > dist[cur_home]:
            continue

        for next_time, next_home in homes[cur_home]:
            if cur_time + next_time < dist[next_home]:
                dist[next_home] = cur_time + next_time
                heappush(pq, (dist[next_home], next_home))

    return dist


def calculate_total_days(dist, max_time):
    pointer = 0
    total_days = 0
    sum_of_time = 0
    # print(dist)
    while pointer < len(dist):
        if dist[pointer] > max_time:
            return -1
        sum_of_time += dist[pointer]
        if sum_of_time == max_time:
            total_days += 1
            sum_of_time = 0
        elif sum_of_time > max_time:
            total_days += 1
            sum_of_time = dist[pointer]
        pointer += 1

    if sum_of_time != 0:
        if dist[pointer - 1] <= max_time:
            total_days += 1

    return total_days


def main():
    stdin = open('./input.txt', 'r')
    num_of_homes, num_of_paths, max_times, my_home = map(int, stdin.readline().split())

    homes = {}
    for home in range(num_of_homes):
        homes[home] = []

    for _ in range(num_of_paths):
        start_home, finish_home, time = map(int, stdin.readline().split())
        homes[start_home].append((time, finish_home))
        homes[finish_home].append((time, start_home))

    dist = dijkstra(homes, my_home)
    dist = [i * 2 for i in dist]
    dist.sort()

    total_days = calculate_total_days(dist[1:], max_times)
    print(total_days)


if __name__ == '__main__':
    main()