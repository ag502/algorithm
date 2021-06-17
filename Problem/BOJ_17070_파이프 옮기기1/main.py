from sys import stdin
from collections import deque

moving_dir = [
    ["right", 0, 1],
    ["down", 1, 0],
    ["cross", 1, 1]
]


class Main:
    def __init__(self):
        self.len_of_house = 0
        self.house = None

        self.main()

    def bfs(self):
        queue = deque()
        queue.append(["right", 0, 1])

        num_of_way = 0
        while queue:
            cur_pipe_dir, cur_pipe_row, cur_pipe_col = queue.popleft()

            if cur_pipe_row == self.len_of_house - 1 and cur_pipe_col == self.len_of_house - 1:
                num_of_way += 1
                continue

            for next_dir, moving_row, moving_col in moving_dir:
                if cur_pipe_dir == "right" and next_dir == "down":
                    continue
                elif cur_pipe_dir == "down" and next_dir == "right":
                    continue

                next_row = cur_pipe_row + moving_row
                next_col = cur_pipe_col + moving_col

                if 0 <= next_row < self.len_of_house and 0 <= next_col < self.len_of_house:
                    if self.house[next_row][next_col] == 1:
                        continue
                    if next_dir == "cross":
                        if self.house[next_row - 1][next_col] == 1 or self.house[next_row][next_col - 1] == 1:
                            continue
                    queue.append([next_dir, next_row, next_col])

        return num_of_way

    def main(self):
        stdin = open("./input.txt", "r")
        self.len_of_house = int(stdin.readline())
        self.house = [list(map(int, stdin.readline().split())) for _ in range(self.len_of_house)]

        if self.house[-1][-1] == 1:
            print(0)
        else:
            print(self.bfs())


if __name__ == '__main__':
    Main()