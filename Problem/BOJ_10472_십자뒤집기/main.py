from sys import stdin


class Main:
    def __init__(self):
        self.board = None

        self.main()

    def main(self):
        stdin = open("./input.txt", "r")
        test_case = int(stdin.readline())

        for _ in range(test_case):
            self.board = [list(stdin.readline().rstrip()) for _ in range(3)]

            print(self.board)


if __name__ == '__main__':
    Main()