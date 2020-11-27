from sys import stdin
from heapq import heappush, heappop

def main():
    stdin = open('./input.txt', 'r')
    num_of_points, num_of_paths = map(int, stdin.readline().split())
    can_go = list(map(int, stdin.readline().split()))

    valley = {}
    for point in  range(num_of_points):
        valley[point] = []

    for _ in range(num_of_paths):
        a, b, t = map(int, stdin.readline().split())
        valley[a].append([b, t])
        valley[b].append([a, t])

    heap = []
    dist = [float('inf')] * num_of_points

    heappush(heap, [0, 0])
    dist[0] = 0

    while len(heap) != 0:
        cur_dist, cur_point = heappop(heap)

        if dist[cur_point] < cur_dist:
            continue

        for next_point, next_dist in valley[cur_point]:
            if next_point != num_of_points - 1 and can_go[next_point] == 1:
                continue
            if dist[next_point] > cur_dist + next_dist:
                dist[next_point] = cur_dist + next_dist
                heappush(heap, [cur_dist + next_dist, next_point])


    if dist[num_of_points - 1] == float('inf'):
        print(-1)
    else:
        print(dist[num_of_points - 1])

if __name__ == '__main__':
    main()