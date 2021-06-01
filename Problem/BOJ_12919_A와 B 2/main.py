from sys import stdin, exit


class Main:
    def __init__(self):
        self.start_string = None
        self.target_string = None
        self.target_string_len = 0

        self.main()

    def process_word(self, cur_string):
        first_char = cur_string[0]
        last_char = cur_string[len(cur_string) - 1]

        if len(cur_string) > len(self.start_string):
            if last_char == 'A':
                self.process_word(cur_string[:len(cur_string) - 1])
            if first_char == 'B':
                self.process_word(cur_string[1:][::-1])
        elif len(cur_string) == len(self.start_string):
            if cur_string == self.start_string:
                print(1)
                exit()

    def main(self):
        stdin = open("./input.txt", "r")
        self.start_string = stdin.readline().rstrip()
        self.target_string = stdin.readline().rstrip()

        self.process_word(self.target_string)
        print(0)


if __name__ == '__main__':
    Main()