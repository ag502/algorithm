from sys import stdin
from heapq import heapify, heappush, heappop


def main():
    num_of_number = int(stdin.readline())
    max_heap = []
    min_heap = []

    for _ in range(num_of_number):
        shout_number = int(stdin.readline())
        if not max_heap:
            heappush(max_heap, (-shout_number, shout_number))
        else:
            if len(max_heap) == len(min_heap):
                heappush(max_heap, (-shout_number, shout_number))
            else:
                heappush(min_heap, shout_number)

            if max_heap[0][1] > min_heap[0]:
                max_value = heappop(max_heap)
                min_value = heappop(min_heap)

                heappush(min_heap, max_value[1])
                heappush(max_heap, (-min_value, min_value))
        print(max_heap[0][1])


if __name__ == "__main__":
    main()
