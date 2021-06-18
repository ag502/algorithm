from sys import stdin
from collections import deque

moving_dir = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0]
]


class Main:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.paint = None
        self.visit = None

        self.main()

    def bfs(self, cur_row, cur_col):
        queue = deque()

        queue.append([cur_row, cur_col])
        self.visit[cur_row][cur_col] = True

        area = 1
        while queue:
            cur_row, cur_col = queue.popleft()

            for moving_row, moving_col in moving_dir:
                next_row = cur_row + moving_row
                next_col = cur_col + moving_col
                if 0 <= next_row < self.rows and 0 <= next_col < self.cols:
                    if self.paint[next_row][next_col] == 1 and not self.visit[next_row][next_col]:
                        area += 1
                        queue.append([next_row, next_col])
                        self.visit[next_row][next_col] = True

        return area

    def main(self):
        stdin = open("./input.txt", "r")
        self.rows, self.cols = map(int, stdin.readline().split())
        self.paint = [list(map(int, stdin.readline().split())) for _ in range(self.rows)]
        self.visit = [[False] * self.cols for _ in range(self.rows)]

        num_of_area = 0
        max_area = 0
        for start_row in range(self.rows):
            for start_col in range(self.cols):
                if not self.visit[start_row][start_col] and self.paint[start_row][start_col] == 1:
                    num_of_area += 1
                    max_area = max(self.bfs(start_row, start_col), max_area)

        print(num_of_area)
        print(max_area)


if __name__ == '__main__':
    Main()