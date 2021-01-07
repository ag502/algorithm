from sys import stdin
from heapq import heappush, heappop
import math


def calculate_dist(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def dijkstra(num_of_plants, max_wire_length, plant_positions, connected_plant_rel):
    dist = [float('inf')] * (num_of_plants + 1)
    parents = [-1] * (num_of_plants + 1)
    pq = []

    dist[1] = 0.0
    heappush(pq, (0.0, 1))

    while len(pq) != 0:
        cur_dist, cur_plant = heappop(pq)

        if cur_dist > dist[cur_plant]:
            continue

        for next_plant in range(1, num_of_plants + 1):
            distance = 0.0
            if ''.join(map(str, sorted([cur_plant, next_plant]))) not in connected_plant_rel:
                distance = calculate_dist(plant_positions[cur_plant], plant_positions[next_plant])

            if distance <= max_wire_length and cur_dist + distance < dist[next_plant]:
                dist[next_plant] = cur_dist + distance
                heappush(pq, (dist[next_plant], next_plant))
                parents[next_plant] = cur_plant
    # print(parents)
    return dist


def main():
    stdin = open('./input.txt', 'r')
    num_of_plants, num_of_remain_wires = map(int, stdin.readline().split())
    max_wire_length = float(stdin.readline())

    # 발전소 위치 저장
    plant_positions = {}
    for plant_num in range(1, num_of_plants + 1):
        x, y = map(int, stdin.readline().split())
        plant_positions[plant_num] = [x, y]

    # 발전소 연결 상태 저장
    connected_plant_relationship = set()
    for _ in range(num_of_remain_wires):
        connected_plants = sorted(list(map(int, stdin.readline().split())))
        connected_plant_relationship.add(''.join(map(str, connected_plants)))

    # print(plant_positions)
    # print(connected_plant_relationship)

    dist = dijkstra(num_of_plants, max_wire_length, plant_positions, connected_plant_relationship)

    if dist[num_of_plants] == float('inf'):
        print(-1)
    else:
        print(math.floor(dist[num_of_plants] * 1000))


if __name__ == '__main__':
    main()