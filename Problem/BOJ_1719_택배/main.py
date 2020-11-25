from sys import stdin
from heapq import heappush, heappop

def main():
    stdin = open('./input.txt', 'r')
    num_of_stock_places, num_of_paths = map(int, stdin.readline().split())
    stock_places = {}
    for i in range(1, num_of_stock_places + 1):
        stock_places[i] = []

    for _ in range(num_of_paths):
        p1, p2, distance = map(int, stdin.readline().split())
        stock_places[p1].append([p2, distance])
        stock_places[p2].append([p1, distance])

    answer = []
    for stock_place in range(1, num_of_stock_places + 1):
        heap = []
        stop_places = []
        dist = [float('inf')] * (num_of_stock_places + 1)

        heappush(heap, [0, stock_place])
        dist[stock_place] = 0

        while len(heap) != 0:
            cur_dist, cur_place = heappop(heap)

            if cur_dist > dist[cur_place]:
                continue

            for next_place, next_dist in stock_places[cur_place]:
                if dist[next_place] > next_dist + cur_dist:
                    dist[next_place] = next_dist + cur_dist
                    heappush(heap, [next_dist + cur_dist, next_place])
                    stop_places.append([cur_place, next_place])
        print(dist)
        answer.append(stop_places)

    print(answer)

if __name__ == '__main__':
    main()