from sys import stdin
from collections import deque


class Main:
    def __init__(self):
        self.years = None
        self.bugs = deque()

        self.main()

    def main(self):
        stdin = open('./input.txt')
        self.years = int(stdin.readline())

        self.bugs.append(3)

        for year in range(2, self.years + 1):
            size = len(self.bugs)
            for _ in range(size):
                cur_bug = self.bugs.popleft()
                if cur_bug != 1:
                    self.bugs.append(cur_bug - 1)
                if year % 2 == 0:
                    self.bugs.append(4)
                else:
                    self.bugs.append(3)

        print(len(self.bugs))


if __name__ == '__main__':
    Main()