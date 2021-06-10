from sys import stdin
from itertools import combinations


class Main:
    def __init__(self):
        self.num_of_numbers = None
        self.target = None
        self.numbers = None
        self.sum_1 = []
        self.sum_2 = []

        self.main()

    def lower_bound(self, target):
        left_ptr = 0
        right_ptr = len(self.sum_2)

        while left_ptr < right_ptr:
            mid = (left_ptr + right_ptr) // 2
            if self.sum_2[mid] < target:
                left_ptr = mid + 1
            else:
                right_ptr = mid
        return right_ptr

    def upper_bound(self, target):
        left_ptr = 0
        right_ptr = len(self.sum_2)

        while left_ptr < right_ptr:
            mid = (left_ptr + right_ptr) // 2
            if self.sum_2[mid] <= target:
                left_ptr = mid + 1
            else:
                right_ptr = mid
        return right_ptr

    def main(self):
        stdin = open("./input.txt", "r")
        self.num_of_numbers, self.target = map(int, stdin.readline().split())
        self.numbers = list(map(int, stdin.readline().split()))

        set_a = self.numbers[:self.num_of_numbers // 2]
        set_b = self.numbers[self.num_of_numbers // 2:]

        for i in range(1, len(set_a) + 1):
            sub_sum_1 = combinations(set_a, i)
            for result in sub_sum_1:
                self.sum_1.append(sum(result))

        for i in range(1, len(set_b) + 1):
            sub_sum_2 = combinations(set_b, i)
            for result in sub_sum_2:
                self.sum_2.append(sum(result))

        self.sum_1.append(0)
        self.sum_2.append(0)

        self.sum_2.sort()

        answer = 0
        for sub_sum in self.sum_1:
            target = self.target - sub_sum
            lower_idx = self.lower_bound(target)
            upper_idx = self.upper_bound(target)
            answer += upper_idx - lower_idx

        if self.target == 0:
            answer -= 1
        print(answer)


if __name__ == '__main__':
    Main()