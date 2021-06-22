from sys import stdin

moving_dir = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
]


class Main:
    def __init__(self):
        self.board = [[0] * 101 for _ in range(101)]

        self.main()

    def main(self):
        stdin = open("./input.txt", "r")
        num_of_recs = int(stdin.readline())

        for _ in range(num_of_recs):
            x, y = map(int, stdin.readline().split())
            for row in range(y, y + 10):
                for col in range(x, x + 10):
                    self.board[row][col] = 1

        answer = 0
        for row in range(100):
            for col in range(100):
                if self.board[row][col] == 1:
                    for moving_row, moving_col in moving_dir:
                        next_row = row + moving_row
                        next_col = col + moving_col
                        if self.board[next_row][next_col] == 0:
                            answer += 1

        print(answer)
        #
        # for row in self.board:
        #     print(''.join(map(str, row)))


if __name__ == '__main__':
    Main()