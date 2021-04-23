from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)


stdin = open("./input.txt", "r")
num_of_node = int(stdin.readline())

-0

visited = [False] * (num_of_node + 1)
parents = [0] * (num_of_node + 1)


def dfs(cur_node):
    visited[cur_node] = True

    for next_node in trees[cur_node]:
        if not visited[next_node]:
            parents[next_node] = cur_node
            dfs(next_node)


def main():
    dfs(1)

    for parent in parents[2:]:
        print(parent)


if __name__ == '__main__':
    main()