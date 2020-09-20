from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

def main():
    N, M = map(int, stdin.readline().split())
    graph = {}
    visited = [0] * (N + 1)

    for i in range(1, N + 1):
        graph[i] = []

    for _ in range(M ):
        u, v = map(int, stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    answer = 0
    for start_node in graph.keys():
        if visited[start_node] != 1:
            dfs(start_node, graph, visited)
            answer += 1
    print(answer)

def dfs(start, graph, visited):
    # 1.체크인
    visited[start] = 1
    # 2.목적지 도착
    # 3.인접노드 순회
    for next_node in graph[start]:
        # 4.갈 수 있는지 검사
        if visited[next_node] != 1:
            dfs(next_node, graph, visited)

if __name__ == '__main__':
    main()