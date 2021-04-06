from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 5)

stdin = open("./input.txt", "r")
num_of_nodes = int(stdin.readline())

visited = [False] * (num_of_nodes + 1)
tree = {}
leaf_nodes = []
start_node = 1
answer = 0


for node in range(1, num_of_nodes + 1):
    tree[node] = []

for _ in range(num_of_nodes - 1):
    start, end, weight = map(int, stdin.readline().split())
    tree[start].append((end, weight))
    tree[end].append((start, weight))


def dfs(cur_node, acc_weight):
    visited[cur_node] = True

    for next_node, next_weight in tree[cur_node]:
        if not visited[next_node]:
            dfs(next_node, acc_weight + next_weight)

    visited[cur_node] = False

    global answer, start_node
    if answer < acc_weight:
        answer = acc_weight
        start_node = cur_node


def main():
    dfs(1, 0)
    global answer
    answer = 0
    dfs(start_node, 0)

    print(answer)


if __name__ == '__main__':
    main()