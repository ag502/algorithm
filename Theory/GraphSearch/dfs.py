vertex = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

adj = {'S': ['A', 'I'],
       'A': ['S', 'B', 'C', 'E', 'G'],
       'B': ['A', 'C', 'D', 'E'],
       'C': ['A', 'B'],
       'D': ['B'],
       'E': ['A', 'B', 'F'],
       'F': ['E'],
       'G': ['A', 'H', 'I'],
       'H': ['G'],
       'I': ['S', 'G']}

visited = {}
for vertex in adj.keys():
    visited[vertex] = False


def dfs(here):
    # 1. 체크인 (방문)
    visited[here] = True
    # 2. 목적지?
    print("DFS visites " + here)
    # 3. 인접한 행렬 순회
    for there in adj[here]:
        # 4. 갈 수 있는 검사
        if not visited[there]:
            dfs(there)

# 모든 정점을 방문한다. (끊어진 정점 포함)
def dfs_all():
    for vertex in adj.keys():
        if not visited[vertex]:
            dfs(vertex)


dfs_all()
