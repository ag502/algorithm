from sys import stdin
from collections import deque
from heapq import heappush, heappop
from math import sqrt, floor


def dijkstra(plants_relations, num_of_plants):
    dist = [float('inf')] * (num_of_plants + 1)
    parents = [-1] * (num_of_plants + 1)
    pq = []

    dist[1] = 0
    heappush(pq, (0, 1))
    parents[1] = 1

    while len(pq) != 0:
        cur_dist, cur_plant = heappop(pq)

        if cur_dist > dist[cur_plant]:
            continue
        for next_dist, next_plant in plants_relations[cur_plant]:
            if cur_dist + next_dist < dist[next_plant]:
                dist[next_plant] = cur_dist + next_dist
                heappush(pq, (dist[next_plant], next_plant))
                parents[next_plant] = cur_plant

    return dist, parents


def shortest_path(parents, cur_plant):
    queue = deque()
    while parents[cur_plant] != cur_plant:
        queue.appendleft(cur_plant)
        cur_plant = parents[cur_plant]

    queue.appendleft(1)
    return queue


def calculate_distance(plant1, plant2):
    x1, y1 = plant1
    x2, y2 = plant2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def main():
    stdin = open('./input.txt', 'r')
    num_of_plants, remain_wires = map(int, stdin.readline().split())
    max_wire_length = float(stdin.readline())

    plants_map = {}
    plant_list = set()
    plants_relations = {}

    for plant in range(1, num_of_plants + 1):
        plants_map[plant] = []
        plants_relations[plant] = []

    for plant in range(1, num_of_plants + 1):
        x, y = map(int, stdin.readline().split())
        plant_list.add(plant)
        plants_map[plant].append(x)
        plants_map[plant].append(y)

    connected_plants = set()
    connected_path = set()
    for _ in range(remain_wires):
        start_plant, finish_plant = map(int, stdin.readline().split())

        distance = calculate_distance(plants_map[start_plant], plants_map[finish_plant])
        plants_relations[start_plant].append((distance, finish_plant))
        plants_relations[finish_plant].append((distance, start_plant))

        connected_plants.add(start_plant)
        connected_plants.add(finish_plant)
        connected_path.add(''.join(map(str,sorted([start_plant, finish_plant]))))

    unconnected_plants = list(plant_list - connected_plants)

    for connected_plant in connected_plants:
        for unconnected_plant in unconnected_plants:
            distance = calculate_distance(plants_map[connected_plant], plants_map[unconnected_plant])
            if distance < max_wire_length:
                plants_relations[connected_plant].append((distance, unconnected_plant))
                plants_relations[unconnected_plant].append((distance, connected_plant))

    for idx_1 in range(len(unconnected_plants) - 1):
        for idx_2 in range(idx_1 + 1, len(unconnected_plants)):
            unconnected_plant1 = unconnected_plants[idx_1]
            unconnected_plant2 = unconnected_plants[idx_2]

        distance = calculate_distance(plants_map[unconnected_plant1], plants_map[unconnected_plant2])
        if distance < max_wire_length:
            plants_relations[unconnected_plant1].append((distance, unconnected_plant2))
            plants_relations[unconnected_plant2].append((distance, unconnected_plant1))

    dist, parents = dijkstra(plants_relations, num_of_plants)
    path = list(shortest_path(parents, num_of_plants))

    sum_of_existed_path = 0
    for plant_1, plant_2 in zip(path, path[1:]):
        if ''.join(map(str, [plant_1, plant_2])) in connected_path:
            sum_of_existed_path += calculate_distance(plants_map[plant_1], plants_map[plant_2])

    print(floor((dist[num_of_plants] - sum_of_existed_path) * 1000))


if __name__ == '__main__':
    main()