from sys import stdin
from collections import deque


def main():
    stdin = open("./input.txt", "r")
    num_of_students = int(stdin.readline())
    t = int(stdin.readline())
    word = int(stdin.readline())

    phase = 1
    student_idx = 0
    count_word = 0
    while True:
        words = deque([0, 1, 0, 1])
        for _ in range(phase + 1):
            words.append(0)
        for _ in range(phase + 1):
            words.append(1)

        while words:
            cur_word = words.popleft()
            if word == 0:
                if cur_word == 0:
                    count_word += 1
            else:
                if cur_word == 1:
                    count_word += 1

            if count_word == t:
                print(student_idx)
                return

            student_idx = (student_idx + 1) % num_of_students
        phase += 1


if __name__ == '__main__':
    main()