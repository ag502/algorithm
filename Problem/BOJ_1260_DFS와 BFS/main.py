from sys import stdin
from collections import deque

# is_visited = None
# a_matrix = None


def main():
    N, M, V = map(int, stdin.readline().split())
    a_matrix = [[0] * (N + 1) for _ in range(N + 1)]

    dfs_answer = []
    bfs_answer = []

    for _ in range(M):
        v_1, v_2 = map(int, stdin.readline().split())
        a_matrix[v_1][v_2] = 1
        a_matrix[v_2][v_1] = 1

    is_visited = [-1] * (N + 1)
    dfs(V, is_visited, a_matrix, dfs_answer)
    print(' '.join(dfs_answer))

    is_visited = [-1] * (N + 1)
    bfs(V, is_visited, a_matrix, bfs_answer)
    print(' '.join(bfs_answer))


def dfs(start_vertex, is_visited, a_matrix, dfs_answer):
    # 1. 체크인
    is_visited[start_vertex] = 0
    # 2. 목적지?
    dfs_answer.append(str(start_vertex))
    # 3. 갈 수 있는 곳을 순회
    for idx, vertex in enumerate(a_matrix[start_vertex][1:]):
        # 4. 갈 수 있는 가?
        if vertex == 1 and is_visited[idx + 1] == -1:
            # 5. dfs(next)
            dfs(idx + 1, is_visited, a_matrix, dfs_answer)
    # 6. 체크아웃
    is_visited[start_vertex] = 1


def bfs(start_vertex, is_visited, a_matrix, bfs_answer):
    queue = deque()
    queue.append(start_vertex)
    is_visited[start_vertex] = 0

    while queue:
        # 1. 큐에서 꺼내옴
        vertex = queue.popleft()
        # 2. 목적지 인가
        bfs_answer.append(str(vertex))
        # 3. 갈 수 있는 곳을 순회
        for idx, vertex in enumerate(a_matrix[vertex][1:]):
            # 4. 갈 수 있는가?
            if vertex == 1 and is_visited[idx + 1] == -1:
                # 5. 체크인
                is_visited[idx + 1] = 0
                queue.append(idx + 1)
                # 6. 큐에 넣음
        is_visited[vertex] = 1


if __name__ == "__main__":
    main()
