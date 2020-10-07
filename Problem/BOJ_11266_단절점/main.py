from sys import stdin

def main():
    v, e = map(int, stdin.readline().split())
    graph = {}
    for i in range(1, v + 1):
        graph[i] = []
    visited = [False] * (v + 1)

    for _ in range(e):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if not visited[i]:
            dfs(graph, visited, i)

    # print(graph)

def dfs(graph, visited, here):
    # 1. 방문
    visited[here] = True
    # 2. 목적지?
    print(here)
    # 3. 갈 수 있는  주변 노드 탐색
    for there in graph[here]:
        # 4. 갈 수 있는지 검사
        if not visited[there]:
            # 5. 간다
            dfs(graph, visited, there)



if __name__ == '__main__':
    main()