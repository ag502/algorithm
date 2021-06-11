from sys import stdin
from collections import deque


class Main:
    def __init__(self):
        self.num_of_elem = None
        self.array_a = deque()
        self.array_b = deque()
        self.array_c = deque()
        self.array_d = deque()

        self.sub_sum_1 = {}
        self.sub_sum_2 = {}

        self.main()

    def lower_bound(self, target):
        left_ptr = 0
        right_ptr = len(self.sub_sum_2)

        while left_ptr < right_ptr:
            mid = (left_ptr + right_ptr) // 2
            if self.sub_sum_2[mid] < target:
                left_ptr = mid + 1
            else:
                right_ptr = mid
        return right_ptr

    def upper_bound(self, target):
        left_ptr = 0
        right_ptr = len(self.sub_sum_2)

        while left_ptr < right_ptr:
            mid = (left_ptr + right_ptr) // 2
            if self.sub_sum_2[mid] <= target:
                left_ptr = mid + 1
            else:
                right_ptr = mid
        return right_ptr

    def main(self):
        stdin = open("./input.txt", "r")
        self.num_of_elem = int(stdin.readline())

        for _ in range(self.num_of_elem):
            line = list(map(int, stdin.readline().split()))
            self.array_a.append(line[0])
            self.array_b.append(line[1])
            self.array_c.append(line[2])
            self.array_d.append(line[3])

        answer = 0
        for a in self.array_a:
            for b in self.array_b:
                self.sub_sum_1[a + b] = self.sub_sum_1.get(a + b, 0) + 1

        for c in self.array_c:
            for d in self.array_d:
                answer += self.sub_sum_1.get(-(c + d), 0)

        print(answer)


if __name__ == '__main__':
    Main()