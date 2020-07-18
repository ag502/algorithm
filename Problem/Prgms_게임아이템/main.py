from heapq import heapify, heappop, heappush
from collections import deque


def solution(healths, items):
    healths.sort()
    items = deque(sorted([(item[1], item[0], idx + 1)
                          for idx, item in enumerate(items)]))
    heap = []
    answer = []

    for health in healths:
        while items:
            debuff, buff, idx = items[0]
            if health - debuff < 100:
                break
            items.popleft()
            heappush(heap, (-buff, idx))
        if heap:
            _, index = heappop(heap)
            answer.append(index)

    return sorted(answer)
