from heapq import heappush, heappop

def solution(n, edge):
    graph = {}
    for node in range(1, n + 1):
        graph[node] = []

    for node_1, node_2 in edge:
        graph[node_1].append(node_2)
        graph[node_2].append(node_1)

    dist = [float('inf')] * (n + 1)
    heap = []

    heappush(heap, [0, 1])
    dist[1] = 0

    while len(heap) != 0:
        cur_dist, cur_node = heappop(heap)

        if dist[cur_node] < cur_dist:
            continue

        for next_node in graph[cur_node]:
            if dist[next_node] > cur_dist + 1:
                dist[next_node] = cur_dist + 1
                heappush(heap, [dist[next_node], next_node])

    answer = 0

    max_dist = 0
    for distance in dist:
        if distance != float('inf') and max_dist < distance:
            max_dist = distance

    for distance in dist:
        if distance == max_dist:
            answer += 1
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))