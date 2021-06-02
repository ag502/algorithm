from sys import stdin


class Main:
    def __init__(self):
        self.docs = []

        self.main()

    def main(self):
        stdin = open("./input.txt", "r")

        while True:
            cur_line = stdin.readline().rstrip()

            if cur_line == "END":
                break

            self.docs.append(cur_line[::-1])

        print('\n'.join(self.docs))


if __name__ == '__main__':
    Main()