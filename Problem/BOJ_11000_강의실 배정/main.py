from sys import stdin
from heapq import heappush, heappop


def main():
    stdin = open("./input.txt", "r")
    num_of_classes = int(stdin.readline())

    classes = []
    for _ in range(num_of_classes):
        start_time, terminate_time = map(int, stdin.readline().split())
        classes.append([start_time, terminate_time])

    heap = []
    classes.sort(key=lambda x: (x[0], x[1]))

    heappush(heap, classes[0][1])

    for class_start_time, class_end_time in classes[1:]:
        top = heap[0]
        if class_start_time >= top:
            heappop(heap)
            heappush(heap, class_end_time)
        else:
            heappush(heap, class_end_time)

    print(len(heap))


if __name__ == '__main__':
    main()