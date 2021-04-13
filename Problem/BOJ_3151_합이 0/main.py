from sys import stdin
from math import floor

stdin = open("./input.txt", "r")

num_of_student = int(stdin.readline())
students = list(map(int, stdin.readline().split()))
students.sort()
answer = 0
print(students)


def lower_bound(target, start, end, a, b):
    global answer
    while start <= end:
        mid = (start + end) // 2
        if target <= students[mid]:
            if target == students[end]:
                print(start, mid, end)
                print(a, b, students[mid])
                answer += 1
            end = mid - 1
        else:
            start = mid + 1

    if start < len(students) and target == students[start]:
        print(start, mid, end)
        print(students[start])
        answer += 1


def main():
    num_of_team = 0
    for i in range(len(students) - 2):
        for j in range(i + 1, len(students) - 1):
            coding_score_1 = students[i]
            coding_score_2 = students[j]
            target = -(coding_score_1 + coding_score_2)
            lower_bound(target, j + 1, len(students) - 1, coding_score_1, coding_score_2)

    print(num_of_team)
    print(answer)


if __name__ == '__main__':
    main()