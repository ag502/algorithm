from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

count = 0

def main():
    v, e = map(int, stdin.readline().split())
    graph = {}
    for i in range(1, v + 1):
        graph[i] = []
    discover = [False] * (v + 1)
    is_cut_vertex = [False] * (v + 1)

    for _ in range(e):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if discover[i] == 0:
           dfs(graph, discover, i, True, is_cut_vertex)

    total_count = 0
    answer = []
    for idx, is_cut in enumerate(is_cut_vertex[1:]):
        if is_cut:
            total_count += 1
            answer.append(str(idx + 1))

    print(total_count)
    print(' '.join(answer))



def dfs(graph, discover, here, is_root, is_cut_vertex):
    # 1. 방문
    global count
    count += 1
    discover[here] = count
    ret = discover[here]
    child = 0

    # 2. 갈 수 있는 곳을 탐색
    for there in graph[here]:
        if discover[there] != 0:
            ret = min(ret, discover[there])
        else:
            child += 1
            low = dfs(graph, discover, there, False, is_cut_vertex)
            if not is_root and low >= discover[here]:
                is_cut_vertex[here] = True
            ret = min(ret, low)

    if is_root:
        is_cut_vertex[here] = (child >= 2)
    return ret


if __name__ == '__main__':
    main()