from sys import stdin
from heapq import heappush, heappop
from math import ceil


def main():
    test_case = int(stdin.readline())

    for _ in range(test_case):
        max_heap = []
        min_heap = []

        length_of_array = int(stdin.readline())
        array = []
        for _ in range(ceil(length_of_array / 10)):
            array += list(map(int, stdin.readline().split()))

        sequence = 0
        answer = []

        for num in array:
            sequence += 1

            if not max_heap:
                heappush(max_heap, (-num, num))
            else:
                if len(max_heap) == len(min_heap):
                    heappush(max_heap, (-num, num))
                else:
                    heappush(min_heap, num)

                if max_heap[0][1] > min_heap[0]:
                    max_value = heappop(max_heap)
                    min_value = heappop(min_heap)

                    heappush(max_heap, (-min_value, min_value))
                    heappush(min_heap, max_value[1])

            if sequence % 2 == 1:
                answer.append(max_heap[0][1])

        ans_string = ''
        for idx, mid_value in enumerate(answer):
            ans_string += str(mid_value)
            if (idx + 1) % 10 == 0:
                ans_string += '\n'
            elif idx != len(answer) - 1:
                ans_string += ' '
        print(len(answer))
        print(ans_string)


if __name__ == "__main__":
    main()
