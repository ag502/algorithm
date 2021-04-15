from sys import stdin

stdin = open("./input.txt", "r")
num_of_vertex, num_of_edge = map(int, stdin.readline().split())
edges = []

for _ in range(num_of_edge):
    vertex_1, vertex_2, cost = map(int, stdin.readline().split())
    edges.append((vertex_1, vertex_2, cost))

edges.sort(key=lambda x: x[2])

parents = [i for i in range(num_of_vertex + 1)]


def find(vertex):
    if vertex == parents[vertex]:
        return vertex
    parents[vertex] = find(parents[vertex])
    return parents[vertex]


def merge(ver_1, ver_2):
    vertex_1_parent = find(ver_1)
    vertex_2_parent = find(ver_2)
    if vertex_1_parent == vertex_2_parent:
        return
    parents[vertex_2_parent] = vertex_1_parent


def main():
    answer = 0
    for ver_1, ver_2, edge_cost in edges:
        # print(ver_1, ver_2, find(ver_1), find(ver_2))
        if find(ver_1) == find(ver_2):
            continue
        merge(ver_1, ver_2)
        answer += edge_cost

    print(answer)


if __name__ == '__main__':
    main()