from sys import stdin
from collections import deque


def main():
    stdin = open("./input.txt", "r")
    num_of_student, num_of_compare = map(int, stdin.readline().split())

    in_degree = [0] * (num_of_student + 1)

    students = {}
    for student in range(1, num_of_student + 1):
        students[student] = []

    for _ in range(num_of_compare):
        student1, student2 = map(int, stdin.readline().split())
        students[student1].append(student2)
        in_degree[student2] += 1

    queue = deque()
    for student, degree in enumerate(in_degree):
        if student != 0 and degree == 0:
            queue.append(student)

    answer = []
    while queue:
        cur_student = queue.popleft()
        answer.append(str(cur_student))

        for next_student in students[cur_student]:
            in_degree[next_student] -= 1
            if in_degree[next_student] == 0:
                queue.append(next_student)

    print(' '.join(answer))


if __name__ == '__main__':
    main()