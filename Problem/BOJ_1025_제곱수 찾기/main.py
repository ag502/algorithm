from sys import stdin


class Main:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.board = []

        self.main()

    def main(self):
        stdin = open("./input.txt", "r")
        self.rows, self.cols = map(int, stdin.readline().split())

        for _ in range(self.rows):
            self.board.append(list(map(int, stdin.readline().rstrip())))

        for row in range(self.rows):
            for col in range(self.cols):
                for common_diff in range(-8, 9):
                    

if __name__ == '__main__':
    Main()