from sys import stdin
from collections import deque

def dfs_recur(adjacency, check, start, res):
    check[start] = True
    res = str(start) + ' '
    for i in range(1, len(adjacency)):
        if adjacency[start][i] == 1 and check[i] == False:
            res += dfs_recur(adjacency, check, i, res)
    return res

def dfs_stack(adjacency, check, start):
    visited_vertex = deque()
    visited_vertex.appendleft(start)
    check[start] = True

    result = (str(start) + ' ')

    while len(visited_vertex) != 0:
        top_vertex = visited_vertex[0]
        flag = False
        for i in range(1, len(adjacency)):
            if adjacency[top_vertex][i] == 1 and check[i] == False:
                visited_vertex.appendleft(i)
                result += str(i) + ' '
                check[i] = True
                flag = True
                break

        if not flag:
            visited_vertex.popleft()

    return result.strip()

def bfs(adjacency, check, start):
    visited_vertex = deque()
    visited_vertex.appendleft(start)
    check[start] = True

    result = ''

    while len(visited_vertex) != 0:
        top_vertex = visited_vertex.popleft()
        result += str(top_vertex) + ' '

        for i in range(1, len(adjacency)):
            if adjacency[top_vertex][i] == 1 and check[i] == False:
                visited_vertex.append(i)
                check[i] = True
    return result.strip()

def main():
    v, e, first_v = map(int, stdin.readline().split())
    adjacency = [[0] * (v + 1) for _ in range(v + 1)]
    check = [False] * (v + 1)

    for _ in range(e):
        start, end = map(int, stdin.readline().split())
        adjacency[start][end] = 1
        adjacency[end][start] = 1

    res = ''
    print(dfs_recur(adjacency, check, first_v, res))

    check = [False] * (v + 1)
    print(dfs_stack(adjacency, check, first_v))

    check = [False] * (v + 1)
    print(bfs(adjacency, check, first_v))

if __name__ == '__main__':
    main()