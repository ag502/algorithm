from sys import stdin


class Main:
    def __init__(self):
        self.password = []
        self.answer = ''

        self.main()

    def main(self):
        stdin = open("./input.txt", "r")

        for _ in range(5):
            self.password.append(stdin.readline().rstrip())

        for i in range(15):
            for j in range(5):
                if i >= len(self.password[j]):
                    continue
                self.answer += self.password[j][i]

        print(self.answer)


if __name__ == '__main__':
    Main()