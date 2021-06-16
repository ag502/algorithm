from sys import stdin
from collections import deque


class Main:
    def __init__(self):
        self.num_of_numbers = None
        self.sequence = None

        self.main()

    def main(self):
        stdin = open("./input.txt", "r")
        self.num_of_numbers = int(stdin.readline())
        self.sequence = [int(stdin.readline()) for _ in range(self.num_of_numbers)]

        stack = deque()
        answer = deque()

        ptr = 0
        for number in range(1, self.num_of_numbers + 1):
            stack.append(number)
            answer.append("+")

            while stack and stack[-1] == self.sequence[ptr]:
                stack.pop()
                answer.append("-")
                ptr += 1

        if stack:
            print("NO")
        else:
            for char in answer:
                print(char)


if __name__ == '__main__':
    Main()