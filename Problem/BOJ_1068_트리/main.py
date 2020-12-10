from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

def dfs(tree, visited, cur_node, leaf_nodes):
    # 방문
    visited[cur_node] = True
    # 주변 탐색
    for next_node in tree[cur_node]:
        if not visited[next_node]:
            dfs(tree, visited, next_node, leaf_nodes)

    # 체크아웃
    visited[cur_node] = False
    if len(tree[cur_node]) == 0:
        leaf_nodes.append(cur_node)

def main():
    stdin = open('./input.txt', 'r')
    num_of_nodes = int(stdin.readline())

    tree = {}
    for node in range(num_of_nodes):
        tree[node] = []

    parents = list(map(int, stdin.readline().split()))
    delete_node = int(stdin.readline())

    root_node = -1
    for idx, parent_node in enumerate(parents):
        if parent_node != -1 and idx != delete_node:
            tree[parent_node].append(idx)
        if parent_node == -1:
            root_node = idx

    visited = [False] * num_of_nodes
    visited[delete_node] = True

    leaf_nodes = []
    if not visited[root_node]:
        dfs(tree, visited, root_node, leaf_nodes)

    print(len(leaf_nodes))

if __name__ == '__main__':
    main()