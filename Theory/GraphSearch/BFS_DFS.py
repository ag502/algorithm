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


def dfs_recur(graph, start):
    is_visited[start] = True
    answer = node_name[start] + ' '

    for i in range(0, len(graph)):
        if graph[start][i] == 1 and not is_visited[i]:
            answer += dfs_recur(graph, i) + ' '
    return answer.rstrip()


def dfs(graph, start):
    stack = deque()
    is_visited = [False] * len(graph)
    stack.appendleft(start)
    is_visited[start] = True

    answer = node_name[start] + ' '

    while stack:
        top_vertex = stack[0]
        for idx, vertex in enumerate(graph[top_vertex]):
            if vertex != 0 and not is_visited[idx]:
                stack.appendleft(idx)
                is_visited[idx] = True
                answer += node_name[idx] + ' '
                break
        else:
            stack.popleft()

    return answer.rstrip()


def bfs(graph, start):
    queue = deque()
    is_visited = [False] * len(graph)
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
    print(dfs(graph, 0))
    print(dfs_recur(graph, 0))
    # bfs(graph, 0, is_visited)
