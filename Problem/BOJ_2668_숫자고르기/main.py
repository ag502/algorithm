from sys import stdin

stdin = open("./input.txt", "r")
N = int(stdin.readline())
graph = {}

for number in range(1, N + 1):
    graph[number] = []
    graph[number].append(int(stdin.readline()))

visited = [False] * (N + 1)
finished = [False] * (N + 1)
parent_nodes = [0] * (N + 1)
cyclic_nodes = set()


def tracking_cycle(cur_node, next_node):
    cyclic_nodes.add(cur_node)
    if cur_node == next_node:
        return
    tracking_cycle(parent_nodes[cur_node], next_node)


def dfs(cur_number):
    visited[cur_number] = True

    for next_number in graph[cur_number]:
        if not visited[next_number]:
            parent_nodes[next_number] = cur_number
            dfs(next_number)
        elif not finished[next_number]:
            tracking_cycle(cur_number, next_number)
    finished[cur_number] = True


def main():
    for cur_number in range(1, N + 1):
        if not visited[cur_number]:
            dfs(cur_number)

    global cyclic_nodes
    cyclic_nodes = list(cyclic_nodes)
    cyclic_nodes.sort()

    print(len(cyclic_nodes))
    for picked_number in cyclic_nodes:
        print(picked_number)


if __name__ == '__main__':
    main()
