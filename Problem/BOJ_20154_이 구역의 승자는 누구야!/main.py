from sys import stdin
from collections import deque

number_of_word_strokes = {
    "A": 3, "B": 2, "C": 1,
    "D": 2, "E": 3, "F": 3,
    "G": 3, "H": 3, "I": 1,
    "J": 1, "K": 3, "L": 1,
    "M": 3, "N": 3, "O": 1,
    "P": 2, "Q": 2, "R": 2,
    "S": 1, "T": 2, "U": 1,
    "V": 1, "W": 2, "X": 2,
    "Y": 2, "Z": 1
}


class Main:
    def __init__(self):
        self.string = deque()

        self.main()

    def main(self):
        stdin = open("./input.txt", "r")

        for char in stdin.readline().rstrip():
            self.string.append(number_of_word_strokes[char])

        while len(self.string) != 1:
            iter_count = len(self.string) // 2
            for _ in range(iter_count):
                char_1 = self.string.popleft()
                char_2 = self.string.popleft()

                result = char_1 + char_2
                if result > 10:
                    result = result % 10
                self.string.append(result)

        last_answer = self.string.popleft()

        if last_answer % 2 == 0:
            print("You're the winner?")
        else:
            print("I'm a winner!")


if __name__ == '__main__':
    Main()