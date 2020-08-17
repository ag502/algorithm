from sys import stdin
from collections import deque


def main():
    N, M = map(int, stdin.readline().split())
    adj = {}
    visited = {}
    for problem_num in range(1, N + 1):
        adj[problem_num] = []
        visited[problem_num] = False

    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        adj[A].append(B)

    adj = dict(sorted(adj.items(), key=lambda x: (-x[0])))
    # print(adj)
    # print(visited)

    records = deque()
    # problems = list(adj.keys())
    for problem in adj.keys():
        # problem = problems[problem]
        if len(adj[problem]) != 0 and not visited[problem]:
            dfs(problem, adj, visited, records)

    # print(records)

    answer = ""
    while records:
        answer += str(records.pop()) + " "

    print(answer.rstrip())


def dfs(here, adj, visited, records):
    # 1. 체크인
    visited[here] = True
    # 2. 방문 (생략)
    # 3. 인접 정점 순회
    for there in adj[here]:
        # 4. 갈 수 있는지 확인
        if not visited[there]:
            dfs(there, adj, visited, records)
    # 5. 체크 아웃
    records.append(here)


if __name__ == "__main__":
    main()
