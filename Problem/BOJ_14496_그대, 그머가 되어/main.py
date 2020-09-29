from sys import stdin
from heapq import heappush, heappop

def main():
    start, finish = map(int, stdin.readline().split())
    n, m = map(int, stdin.readline().split())

    char_graph = {}
    dist = [1001] * (n + 1)
    pq = []

    for i in range(1, n + 1):
        char_graph[i] = []

    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        char_graph[a].append(b)
        char_graph[b].append(a)

    heappush(pq, [0, start])
    dist[start] = 0

    while len(pq) != 0:
        distance, cur_char = heappop(pq)

        if distance > dist[cur_char]:
            continue

        for next_char in char_graph[cur_char]:
            if distance + 1 < dist[next_char]:
                heappush(pq, [distance + 1, next_char])
                dist[next_char] = distance + 1

    print(-1 if dist[finish] >= 1001 else dist[finish])

if __name__ == '__main__':
    main()
