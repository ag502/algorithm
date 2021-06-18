from sys import stdin, maxsize


class Main:
    def __init__(self):
        self.start_num = 0
        self.target_num = 0
        self.number_set = set()
        self.answer = float("INF")

        self.main()

    def find_number(self, cur_num, operation_count):
        self.number_set.add(cur_num)

        if cur_num < self.target_num:
            multiple_number = cur_num * 2
            if multiple_number not in self.number_set:
                self.find_number(multiple_number, operation_count + 1)
            append_number = cur_num * 10 + 1
            if append_number not in self.number_set:
                self.find_number(append_number, operation_count + 1)
        elif cur_num == self.target_num:
            self.answer = min(self.answer, operation_count)
        self.number_set.discard(cur_num)

    def main(self):
        stdin = open("./input.txt", "r")
        self.start_num, self.target_num = map(int, stdin.readline().split())

        self.find_number(self.start_num, 0)
        print(-1 if self.answer == float("INF") else self.answer + 1)


if __name__ == '__main__':
    Main()