from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

def dfs(tree, visited, parents, cur_node, prev_node):
    # 방문
    visited[cur_node] = True
    if cur_node != 1:
        parents[cur_node] = prev_node

    # 주변 탐색
    for next_node in tree[cur_node]:
        if not visited[next_node]:
            dfs(tree, visited, parents, next_node, cur_node)

    # 체크아웃
    visited[cur_node] = False


def main():
    stdin = open('./input.txt', 'r')
    num_of_nodes = int(stdin.readline())

    tree = {}
    for node in range(1, num_of_nodes + 1):
        tree[node] = []

    for _ in range(num_of_nodes - 1):
        node_1, node_2 = map(int, stdin.readline().split())
        tree[node_1].append(node_2)
        tree[node_2].append(node_1)

    visited = [False] * (num_of_nodes + 1)
    parent = [-1] * (num_of_nodes + 1)

    dfs(tree, visited, parent, 1, None)

    for parent_node in parent[2:]:
        print(parent_node)

if __name__ == '__main__':
    main()
