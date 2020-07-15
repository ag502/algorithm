from collections import deque

graph = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0]
]

node_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

is_visited = [False] * 9


def dfs(graph, start, is_visited):
    stack = deque()
    stack.append(start)
    is_visited[start] = True

    while stack:
        current_node = stack.pop()
        print(node_name[current_node])
        for idx, node in enumerate(graph[current_node]):
            if node != 0 and is_visited[idx] == False:
                stack.append(idx)
                is_visited[idx] = True


def bfs(graph, start, is_visited):
    queue = deque()
    queue.append(start)
    is_visited[start] = True
    while queue:
        current_node = queue.popleft()
        print(node_name[current_node])

        for idx, node in enumerate(graph[current_node]):
            if node != 0 and is_visited[idx] == False:
                queue.append(idx)
                is_visited[idx] = True


if __name__ == "__main__":
    # dfs(graph, 0, is_visited)
    bfs(graph, 0, is_visited)
