from sys import stdin, setrecursionlimit
setrecursionlimit(100000)

count = 0
def main():
    v, e = map(int, stdin.readline().split())
    graph = {}
    for i in range(1, v + 1):
        graph[i] = []

    for _ in range(e):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    discover = [0] * (v + 1)
    is_cur = set()

    for i in range(1, v + 1):
        if discover[i] == 0:
            dfs(graph, discover, is_cur, i, 0)

    is_cur = sorted(is_cur)
    print(len(is_cur))
    for edge in is_cur:
        print(' '.join(map(str, edge)))

def dfs(graph, discover, is_cur, here, parent):
    # 1. 방문
    global count
    count += 1
    discover[here] = count
    ret = discover[here]

    # 2. 갈 수 있는 곳 검사
    for there in graph[here]:
        if there == parent:
            continue
        if discover[there] == 0:
            low = dfs(graph, discover, is_cur, there, here)
            if low > discover[here]:
                is_cur.add((min(here, there), max(here, there)))

            ret = min(ret, low)
        else:
            ret = min(ret, discover[there])

    return ret

if __name__ == '__main__':
    main()