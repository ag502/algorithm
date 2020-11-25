from sys import stdin
from heapq import heappush, heappop

def main():
    stdin = open('./input.txt', 'r')
    num_of_short_cuts, length_of_road = map(int, stdin.readline().split())
    road_points = {}

    for point in range(length_of_road + 1):
        if point == length_of_road:
            road_points[point] = []
        else:
            road_points[point] = [[1, point + 1]]

    for _ in range(num_of_short_cuts):
        start_point, end_point, distance = map(int, stdin.readline().split())
        if start_point > length_of_road or end_point > length_of_road:
            continue
        road_points[start_point].append([distance, end_point])

    dist = [float('inf')] * (length_of_road + 1)
    heap = [[0, 0]]
    dist[0] = 0

    while len(heap) != 0:
        cur_dist, cur_point = heappop(heap)

        if dist[cur_point] < cur_dist:
            continue
        for next_dist, next_point in road_points[cur_point]:
            if dist[next_point] > cur_dist + next_dist:
                dist[next_point] = cur_dist + next_dist
                heappush(heap, [cur_dist + next_dist, next_point])

    print(dist[length_of_road])

if __name__ == '__main__':
    main()