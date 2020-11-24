from sys import stdin
from heapq import heappush, heappop

def main():
    stdin = open('./input.txt', 'r')
    test_case = int(stdin.readline())

    for _ in range(test_case):
        num_of_comps, num_of_dep, hacked_com = map(int, stdin.readline().split())

        computers = {}
        for computer in range(1, num_of_comps + 1):
            computers[computer] = []

        dist = [float('inf')] * (num_of_comps + 1)

        for _ in range(num_of_dep):
            a, b, s = map(int, stdin.readline().split())
            computers[b].append([a, s])

        heap = []
        heappush(heap, [0, hacked_com])
        dist[hacked_com] = 0

        while len(heap) != 0:
            cur_dist, cur_computer = heappop(heap)

            if cur_dist > dist[cur_computer]:
                continue

            for next_computer, next_dist in computers[cur_computer]:
                if dist[next_computer] > next_dist + cur_dist:
                    dist[next_computer] = min(dist[next_computer], next_dist + cur_dist)
                    heappush(heap, [dist[next_computer], next_computer])

        hacked_computers = 0
        time = 0
        for distance in dist[1:]:
            if distance != float('inf'):
                hacked_computers += 1
                if distance > time:
                    time = distance
        print(str(hacked_computers) + " " + str(time))

if __name__ == '__main__':
    main()