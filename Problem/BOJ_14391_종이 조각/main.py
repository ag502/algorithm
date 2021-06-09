from sys import stdin, maxsize

direction = ["ROW", "COL"]

class Main:
    def __init__(self):
        stdin = open("./input.txt", "r")
        self.rows, self.cols = map(int, stdin.readline().split())
        self.paper = [list(stdin.readline().rstrip()) for _ in range(self.rows)]
        self.visited = [[False] * self.cols for _ in range(self.rows)]
        self.acc_area = 0
        self.total_area = self.rows * self.cols
        self.numbers = []
        self.answer = -maxsize

        self.main()

    def check_validation(self, cur_row, cur_col, cur_dir, count):
        if cur_dir == "ROW":
            for i in range(count + 1):
                if cur_col + i >= self.cols or self.visited[cur_row][cur_col + i]:
                    return False
            return True
        elif cur_dir == "COL":
            for i in range(count + 1):
                if cur_row + i >= self.rows or self.visited[cur_row + i][cur_col]:
                    return False
            return True

    def make_partition(self, cur_row, cur_col, cur_dir, count, cur_nums=[], temp=[]):
        number = ""

        if cur_dir == "ROW":
            for i in range(count + 1):
                self.visited[cur_row][cur_col + i] = True
                number += self.paper[cur_row][cur_col + i]
                temp.append([cur_row, cur_col + i, cur_dir, count + 1])

        elif cur_dir == "COL":
            for i in range(count + 1):
                self.visited[cur_row + i][cur_col] = True
                number += self.paper[cur_row + i][cur_col]
                temp.append([cur_row + i, cur_col, cur_dir, count + 1])

        cur_nums.append(number)
        self.acc_area += (count + 1)

        if self.acc_area < self.total_area:
            for next_row in range(self.rows):
                for next_col in range(self.cols):
                    for next_count in range(max(self.rows, self.cols)):
                        if next_count == 0:
                            if self.check_validation(next_row, next_col, "ROW", next_count):
                                self.make_partition(next_row, next_col, "ROW", next_count)
                        else:
                            if self.check_validation(next_row, next_col, "ROW", next_count):
                                self.make_partition(next_row, next_col, "ROW", next_count, cur_nums, temp)
                            if self.check_validation(next_row, next_col, "COL", next_count):
                                self.make_partition(next_row, next_col, "COL", next_count, cur_nums, temp)
        elif self.acc_area == self.total_area:
            print(cur_nums)
            print(temp)
            self.answer = max(self.answer, sum(map(int, cur_nums)))

        if cur_dir == "ROW":
            for i in range(count + 1):
                self.visited[cur_row][cur_col + i] = False
                temp.pop()
        elif cur_dir == "COL":
            for i in range(count + 1):
                self.visited[cur_row + i][cur_col] = False
                temp.pop()

        cur_nums.pop()
        self.acc_area -= (count + 1)

    def main(self):
        for start_row in range(self.rows):
            for start_col in range(self.cols):
                for start_dir in range(2):
                    for start_count in range(max(self.rows, self.cols)):
                        if self.check_validation(start_row, start_col, direction[start_dir], start_count):
                            self.make_partition(start_row, start_col, direction[start_dir], start_count)

        print(self.answer)


if __name__ == '__main__':
    Main()