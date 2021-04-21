from sys import stdin
from collections import deque


def main():
    stdin = open("./input.txt", "r")
    num_of_subject, num_of_condition = map(int, stdin.readline().split())

    subjects = {}
    for subject in range(1, num_of_subject + 1):
        subjects[subject] = []

    in_degree = [0] * (num_of_subject + 1)

    for _ in range(num_of_condition):
        pre_subject, next_subject = map(int, stdin.readline().split())
        subjects[pre_subject].append(next_subject)
        in_degree[next_subject] += 1

    queue = deque()
    for subject, degree in enumerate(in_degree):
        if subject != 0 and degree == 0:
            queue.append(subject)

    answer = [0] * (num_of_subject + 1)
    semester = 0
    while queue:
        size = len(queue)
        semester += 1
        for _ in range(size):
            cur_subject = queue.popleft()
            answer[cur_subject] = semester

            for next_subject in subjects[cur_subject]:
                in_degree[next_subject] -= 1
                if in_degree[next_subject] == 0:
                    queue.append(next_subject)

    print(' '.join(map(str, answer[1:])))


if __name__ == '__main__':
    main()