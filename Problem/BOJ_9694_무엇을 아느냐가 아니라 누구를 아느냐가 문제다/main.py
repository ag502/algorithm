from sys import stdin
from heapq import heappush, heappop

def dijkstra(relations, num_of_politician):
    dist = [float('inf')] * num_of_politician
    heap = []

    dist[0] = 0
    heappush(heap, [0, 0])

    while len(heap) != 0:
        cur_dist, cur_politician = heappop(heap)

        if dist[cur_politician] > cur_dist:
            continue

        for next_politician_info in relations[cur_politician]:
            next_politician, next_dist = next_politician_info['politician'], next_politician_info['type']
            if dist[next_politician] > cur_dist + next_dist:
                dist[next_politician] = cur_dist + next_dist
                heappush(heap, [dist[next_politician], next_politician])
    return dist

def dfs(relations, visited, cur_politician, acc_dist, max_dist, path, final_politician, answer):
    # 1. 방문
    visited[cur_politician] = True
    # 2. 도착
    path.append(cur_politician)
    # 3. 주위 탐색
    for next_politician_info in relations[cur_politician]:
        next_politician, next_dist = next_politician_info['politician'], next_politician_info['type']
        if not visited[next_politician] and acc_dist + next_dist <= max_dist:
            dfs(relations, visited, next_politician, acc_dist + next_dist, max_dist, path, final_politician, answer)
    # 4. 체크아웃
    if acc_dist == max_dist and cur_politician == final_politician:
        answer = path[:]
        print(answer)
    visited[cur_politician] = False
    path.pop()

def main():
    stdin = open('./input.txt', 'r')
    test_case = int(stdin.readline())

    for t in range(test_case):
        num_of_relations, num_of_politician = map(int, stdin.readline().split())

        relations = {}
        for politician in range(num_of_politician):
            relations[politician] = []

        for _ in range(num_of_relations):
            p1, p2, relations_type = map(int, stdin.readline().split())
            relations[p1].append({'politician': p2, 'type': relations_type})
            relations[p2].append({'politician': p1, 'type': relations_type})

        dist = dijkstra(relations, num_of_politician)

        if dist[num_of_politician - 1] == float('inf'):
            print('Case #{}: -1'.format(t + 1))
        else:
            visited = [False] * num_of_politician
            answer = []
            dfs(relations, visited, 0, 0, dist[num_of_politician - 1], [], num_of_politician - 1, answer)
            print(answer)

if __name__ == '__main__':
    main()