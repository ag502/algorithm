from sys import stdin


class Main:
    def __init__(self):
        self.content = ''
        self.keyword = ''

        self.main()

    def main(self):
        stdin = open("./input.txt", "r")
        self.content = stdin.readline().rstrip()
        self.keyword = stdin.readline().rstrip()

        parsed_content = ''
        for char in self.content:
            if char.isdigit():
                continue
            parsed_content += char

        if self.keyword in parsed_content:
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    Main()