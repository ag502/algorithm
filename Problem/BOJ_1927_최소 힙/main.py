from sys import stdin
import heapq

def main():
    num_of_number = int(stdin.readline())
    heap = []

    for _ in range(num_of_number):
        input_number = int(stdin.readline())
        if input_number == 0:
            if len(heap) == 0:
                print(0)
            else:
                print(heapq.heappop(heap))
        else:
            heapq.heappush(heap, input_number)

if __name__ == '__main__':
    main()