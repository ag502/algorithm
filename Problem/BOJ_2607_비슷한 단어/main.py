from sys import stdin
from collections import deque


class Main:
    def __init__(self):
        self.target = [0] * 26

        self.main()

    def check_word(self, comparable):
        len_of_target = 0
        len_of_comparable = 0
        char_diff = 0

        for target_count, comparable_count in zip(self.target, comparable):
            len_of_target += target_count
            len_of_comparable += comparable_count

            char_diff += abs(target_count - comparable_count)

        if abs(len_of_target - len_of_comparable) <= 1 and char_diff <= 2:
            return True
        return False

    def main(self):
        stdin = open("./input.txt", "r")
        num_of_words = int(stdin.readline())

        target_word = stdin.readline().rstrip()
        for char in target_word:
            self.target[ord(char) - ord('A')] += 1

        answer = 0
        for _ in range(num_of_words - 1):
            comparable_word = stdin.readline().rstrip()
            comparable = [0] * 26

            for char in comparable_word:
                comparable[ord(char) - ord('A')] += 1

            if self.check_word(comparable):
                answer += 1

        print(answer)


if __name__ == '__main__':
    Main()