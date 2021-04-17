from sys import stdin


def main():
    stdin = open("./input.txt", "r")
    students = set([i for i in range(1, 31)])

    for _ in range(28):
        student = int(stdin.readline())
        students.discard(student)

    array_students = list(students)
    array_students.sort()
    print(array_students[0])
    print(array_students[1])


if __name__ == '__main__':
    main()