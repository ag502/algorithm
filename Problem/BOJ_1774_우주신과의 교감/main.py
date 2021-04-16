from sys import stdin
from heapq import heappush, heappop

stdin = open("./input.txt", "r")
num_of_god, num_of_connected_path = map(int, stdin.readline().split())

positions = []
for _ in range(num_of_god):
    positions.append(list(map(int, stdin.readline().split())))

connected_gods = []
for _ in range(num_of_connected_path):
    connected_gods.append(list(map(int, stdin.readline().split())))

parents = [i for i in range(num_of_god + 1)]


def get_dist(x1, y1, x2, y2):
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5


def find(god):
    if god == parents[god]:
        return god
    parents[god] = find(parents[god])
    return parents[god]


def merge(god1, god2):
    god1_parent = find(god1)
    god2_parent = find(god2)
    if god1_parent == god2_parent:
        return
    parents[god2_parent] = god1_parent


def main():
    heap = []
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            x1, y1 = positions[i]
            x2, y2 = positions[j]
            heappush(heap, (get_dist(x1, y1, x2, y2), (i + 1), (j + 1)))

    for god1, god2 in connected_gods:
        merge(god1, god2)

    answer = 0
    while heap:
        dist, god1, god2 = heappop(heap)
        if find(god1) == find(god2):
            continue
        merge(god1, god2)
        answer += dist

    print("%.2f" % answer)


if __name__ == '__main__':
    main()