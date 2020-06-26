from sys import stdin
from collections import deque

def dfs_recur(adjacency, check, start):
    check[start] = True
    res = str(start) + ' '
    if start in adjacency:
        for vertex in adjacency[start]:
            if not check[vertex]:
               res += dfs_recur(adjacency, check, vertex)
    return res

def dfs_stack(adjacency, check, start):
    visited_vertex = deque()
    visited_vertex.appendleft(start)
    check[start] = True
    res = str(start) + ' '

    while len(visited_vertex) != 0:
        top_vertex = visited_vertex[0]
        flag = False
        if top_vertex in adjacency:
            for vertex in adjacency[top_vertex]:
                if not check[vertex]:
                    visited_vertex.appendleft(vertex)
                    check[vertex] = True
                    res += str(vertex) + ' '
                    flag = True
                    break

        if not flag:
            visited_vertex.popleft()

    return res

def bfs(adjacency, check, start):
    visited_vertex = deque()
    visited_vertex.append(start)
    check[start] = True
    res = ''

    while len(visited_vertex) != 0:
        top_vertex = visited_vertex.popleft()
        res += str(top_vertex) + ' '
        if top_vertex in adjacency:
            for vertex in adjacency[top_vertex]:
                if not check[vertex]:
                    visited_vertex.append(vertex)
                    check[vertex] = True
    return res

def main():
    v, e, start_vertex = map(int, stdin.readline().split())
    adjacency_list = {}
    # check = [False] * (v + 1)

    for _ in range(e):
        start, end = map(int, stdin.readline().split())
        if start not in adjacency_list:
            adjacency_list[start] = []
        if end not in adjacency_list:
            adjacency_list[end] = []
        adjacency_list[start].append(end)
        adjacency_list[end].append(start)

    for key in adjacency_list:
        adjacency_list[key] = sorted(set(adjacency_list[key]))

    # print(adjacency_list)
    #
    # res = dfs_recur(adjacency_list, check, start_vertex)
    # print(res.strip())

    check = [False] * (v + 1)
    res = dfs_stack(adjacency_list, check, start_vertex)
    print(res.strip())

    check = [False] * (v + 1)
    res = bfs(adjacency_list, check, start_vertex)
    print(res.strip())

if __name__ == '__main__':
    main()