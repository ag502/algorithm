from sys import stdin
from collections import deque

# is_visited = None
# a_matrix = None


def main():
    N, M, V = map(int, stdin.readline().split())
    a_matrix = [[0] * (N + 1) for _ in range(N + 1)]
    is_visited = [False] * (N + 1)

    for _ in range(M):
        v_1, v_2 = map(int, stdin.readline().split())
        a_matrix[v_1][v_2] = 1
        a_matrix[v_2][v_1] = 1

    dfs(V, is_visited, a_matrix)


def dfs(start_vertex, is_visited, a_matrix):
    # 1. 체크인
    is_visited[start_vertex] = False
    # 2. 목적지?
    print(start_vertex)
    # 3. 갈 수 있는 곳을 순회
    for idx, vertex in enumerate(a_matrix[start_vertex][1:]):
        # 4. 갈 수 있는 가?
        if vertex == 1 and not is_visited[idx + 1]:
            is_visited[idx + 1] = True
            # 5. dfs(next)
            dfs(idx + 1, is_visited, a_matrix)
    # 6. 체크아웃
    # is_visited[start_vertex] = False


if __name__ == "__main__":
    main()
