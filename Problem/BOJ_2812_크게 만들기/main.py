from sys import stdin
from heapq import heappush, heappop


def main():
    stdin = open('./input.txt', 'r')
    num_of_digits, num_of_delete_digits = map(int, stdin.readline().split())
    number = map(int, stdin.readline())

    heap = []
    for idx, digit in enumerate(number):
        heappush(heap, (digit, idx))

    for _ in range(num_of_delete_digits):
        heappop(heap)

    heap.sort(key=lambda x: x[1])

    answer = ''
    for digit, idx in heap:
        answer += str(digit)

    print(answer)


if __name__ == '__main__':
    main()