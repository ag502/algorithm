from sys import stdin
from heapq import heappush, heappop


class Main:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.delete_max_heap = []
        self.delete_min_heap = []

        self.main()

    def main(self):
        stdin = open("./input.txt", "r")
        test_case = int(stdin.readline())

        for _ in range(test_case):
            num_of_operation = int(stdin.readline())

            self.max_heap.clear()
            self.min_heap.clear()
            self.delete_max_heap.clear()
            self.delete_min_heap.clear()

            for _ in range(num_of_operation):
                instruction, number = stdin.readline().split()
                if instruction == "I":
                    heappush(self.min_heap, int(number))
                    heappush(self.max_heap, -int(number))
                elif instruction == "D":
                    if int(number) == -1:
                        while len(self.delete_min_heap) != 0 and self.delete_min_heap[0] == self.min_heap[0]:
                            heappop(self.min_heap)
                            heappop(self.delete_min_heap)

                        if len(self.min_heap) != 0:
                            deleted_num = heappop(self.min_heap)
                            heappush(self.delete_max_heap, -deleted_num)
                    elif int(number) == 1:
                        while len(self.delete_max_heap) != 0 and self.delete_max_heap[0] == self.max_heap[0]:
                            heappop(self.max_heap)
                            heappop(self.delete_max_heap)

                        if len(self.max_heap) != 0:
                            deleted_num = heappop(self.max_heap)
                            heappush(self.delete_min_heap, -deleted_num)

            min_value = None
            while self.min_heap:
                cur_min_value = heappop(self.min_heap)
                if self.delete_min_heap and self.delete_min_heap[0] == cur_min_value:
                    heappop(self.delete_min_heap)
                    continue
                min_value = cur_min_value
                break

            max_value = None
            while self.max_heap:
                cur_max_value = heappop(self.max_heap)
                if self.delete_max_heap and self.delete_max_heap[0] == cur_max_value:
                    heappop(self.delete_max_heap)
                    continue
                max_value = cur_max_value
                break

            if min_value is None or max_value is None:
                print("EMPTY")
            else:
                print("%s %s" % (-max_value, min_value))


if __name__ == '__main__':
    Main()