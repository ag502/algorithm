import heapq

def solution(no, works):
    heap = []
    for work in works:
        heap.append((-work, work))

    heapq.heapify(heap)
    while no >= 1:
        biggest_work = heapq.heappop(heap)
        if biggest_work[1] <= 0:
            break

        heapq.heappush(heap, (biggest_work[0] + 1, biggest_work[1] - 1))
        no -= 1

    result = 0
    for elem in heap:
        result += elem[1] ** 2

    return result