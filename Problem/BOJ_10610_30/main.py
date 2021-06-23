from sys import stdin


class Main:
    def __init__(self):
        self.target_number = ''

        self.main()

    def main(self):
        stdin = open("./input.txt", "r")
        self.target_number = list(map(int, stdin.readline().rstrip()))

        sum_of_digit = sum(self.target_number)
        self.target_number.sort(key=lambda x: -x)

        if sum_of_digit % 3 != 0:
            print(-1)
            return
        if self.target_number[-1] != 0:
            print(-1)
            return

        print(''.join(map(str, self.target_number)))


if __name__ == '__main__':
    Main()