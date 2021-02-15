from sys import stdin, maxsize, setrecursionlimit
setrecursionlimit(10000)


def dfs(cur_island, weight, cur_weight, visited):
    visited[cur_island] = True

    for next_island, next_weight in graph[cur_island]:
        if cur_island != end and next_weight >= cur_weight and not visited[next_island]:
            return dfs(next_island, next_weight, cur_weight, visited)

    if cur_island == end:
        return True
    # if weight < cur_weight:
    #     return False
    visited[cur_island] = False
    return False


def binary_search():
    left = 0
    right = 1000000000
    b = 0
    while left <= right:
        visited = [False] * (num_of_island + 1)
        mid = (left + right) // 2
        a = dfs(start, maxsize, mid, visited)
        if a:
            b = mid
            left = mid + 1
        else:
            right = mid - 1
    return b


def main():
    stdin = open('input.txt', 'r')
    global num_of_island, num_of_bridge, graph, start, end, answer

    num_of_island, num_of_bridge = map(int, stdin.readline().split())

    graph = {}
    for island in range(1, num_of_island + 1):
        graph[island] = []

    for _ in range(num_of_bridge):
        start_island, end_island, weight_limit = map(int, stdin.readline().split())
        graph[start_island].append([end_island, weight_limit])
        graph[end_island].append([start_island, weight_limit])

    start, end = map(int, stdin.readline().split())

    print(binary_search())


if __name__ == '__main__':
    main()