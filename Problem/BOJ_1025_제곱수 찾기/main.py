from sys import stdin


class Main:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.board = []
        self.common_diff = set()
        self.answer = set()

        self.main()

    def main(self):
        stdin = open("./input.txt", "r")

        self.rows, self.cols = map(int, stdin.readline().split())
        for _ in range(self.rows):
            self.board.append(list(map(int, stdin.readline().rstrip())))

        for row_diff in range(-self.rows, self.rows):
            for col_diff in range(-self.cols, self.cols):
                self.common_diff.add((row_diff, col_diff))

        for row in range(self.rows):
            for col in range(self.cols):
                for cur_diff in self.common_diff:
                    sequence = []
                    next_row = row
                    next_col = col

                    if cur_diff[0] == 0 and cur_diff[1] == 0:
                        self.answer.add(str(self.board[row][col]))
                        continue

                    while 0 <= next_row < self.rows and 0 <= next_col < self.cols:
                        sequence.append(self.board[next_row][next_col])
                        string = ''.join(map(str, sequence))
                        self.answer.add(string)

                        next_row += cur_diff[0]
                        next_col += cur_diff[1]

        answer = -1
        for number in self.answer:
            number = int(number)
            if int(number ** 0.5) ** 2 == number:
                answer = max(answer, number)

        print(answer)


if __name__ == '__main__':
    Main()
