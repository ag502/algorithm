adj = {
    'A': ['B', 'G'],
    'B': ['A', 'F'],
    'G': ['A'],
    'C': ['E', 'F'],
    'D': ['C', 'E'],
    'E': ['C', 'D', 'H'],
    'H': ['C', 'E'],
    'F': ['B']
}

visited = {}
for vertex in adj.keys():
    visited[vertex] = False


def dfs(here):
    # 1. 체크인
    visited[here] = True
    # 2. 목적지
    print("DFS visits " + here)
    # 3. 인접한 정점 순회
    for there in adj[here]:
        # 4. 갈 수 있는지 검사
        if not visited[there]:
            dfs(there)


def dfs_all():
    sub_sets = []
    element_set = set()
    for vertex in adj.keys():
        if not visited[vertex]:
            dfs(vertex)
            sub_set = []
            for vertex, boolean in visited.items():
                if vertex not in element_set and boolean is True:
                    element_set.add(vertex)
                    sub_set.append(vertex)
            sub_sets.append(sub_set)
    print(sub_sets)


dfs_all()
