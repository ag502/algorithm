from sys import stdin
from collections import deque


def main():
    num_of_computer = int(stdin.readline())
    num_of_connection = int(stdin.readline())

    a_matrix = [[0] * (num_of_computer + 1)
                for _ in range(num_of_computer + 1)]

    for _ in range(num_of_connection):
        vx_1, vx_2 = map(int, stdin.readline().split())
        a_matrix[vx_1][vx_2] = 1
        a_matrix[vx_2][vx_1] = 1

    # is_visited = [-1] * (num_of_computer + 1)
    # infected = []
    # dfs(1, a_matrix, is_visited, infected)
    # print(len(infected) - 1)

    is_visited = [-1] * (num_of_computer + 1)
    infected = []
    bfs(1, a_matrix, is_visited, infected)
    print(len(infected) - 1)


def dfs(start, a_matrix, is_visited, infected):
    # 1. 체크인
    is_visited[start] = 0
    # 2. 목적지?
    infected.append(start)
    # 3. 갈 수 있는 곳을 순회
    for idx, vertex in enumerate(a_matrix[start][1:]):
        # 4. 갈 수 있는 지 검사
        if vertex == 1 and is_visited[idx + 1] == -1:
            # 5. 간다
            dfs(idx + 1, a_matrix, is_visited, infected)
    # 4. 체크 아웃
    is_visited[start] = 1


def bfs(start, a_matrix, is_visited, infected):
    queue = deque()
    queue.append(start)
    is_visited[start] = 0

    while queue:
        # 1. 큐에서 꺼냄
        current_vertex = queue.popleft()
        # 2. 목적지
        infected.append(current_vertex)
        # 3. 갈 수 있는 곳을 순회
        for idx, vertex in enumerate(a_matrix[current_vertex][1:]):
            # 4. 갈 수 있는 지 검사
            if vertex == 1 and is_visited[idx + 1] == -1:
                # 5. 큐에 넣어 줌
                queue.append(idx + 1)
                is_visited[idx + 1] = 0
        is_visited[current_vertex] = 1


if __name__ == "__main__":
    main()
