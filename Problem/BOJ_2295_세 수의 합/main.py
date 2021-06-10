from sys import stdin
from collections import deque


class Main:
    def __init__(self):
        self.num_of_elem = None
        self.set = None
        self.sum_1 = deque()
        self.sum_2 = deque()

        self.main()

    def lower_bound(self, target):
        left_ptr = 0
        right_ptr = len(self.sum_2)

        while left_ptr < right_ptr:
            mid = (left_ptr + right_ptr) // 2
            if self.sum_2[mid][1] < target:
                left_ptr = mid + 1
            elif self.sum_2[mid][1] >= target:
                right_ptr = mid
        return right_ptr

    def upper_bound(self, target):
        left_ptr = 0
        right_ptr = len(self.sum_2)

        while left_ptr < right_ptr:
            mid = (left_ptr + right_ptr) // 2
            if self.sum_2[mid][1] <= target:
                left_ptr = mid + 1
            elif self.sum_2[mid][1] > target:
                right_ptr = mid
        return right_ptr

    def main(self):
        stdin = open("./input.txt", "r")
        self.num_of_elem = int(stdin.readline())
        self.set = [int(stdin.readline()) for _ in range(self.num_of_elem)]
        self.set.sort()

        for x in range(self.num_of_elem):
            for y in range(x, self.num_of_elem):
                self.sum_1.append(self.set[x] + self.set[y])

        for k in self.set:
            for z in self.set:
                if k < z:
                    break
                self.sum_2.append([k, k - z])

        self.sum_2 = list(self.sum_2)
        self.sum_2.sort(key=lambda x: x[1])

        answer = 0
        for sub_sum in self.sum_1:
            lower_idx = self.lower_bound(sub_sum)
            upper_idx = self.upper_bound(sub_sum)

            if lower_idx != upper_idx:
                answer = max(answer, self.sum_2[upper_idx - 1][0])

        print(answer)


if __name__ == '__main__':
    Main()