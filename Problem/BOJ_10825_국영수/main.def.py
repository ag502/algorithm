from sys import stdin


def main():
    student_number = int(stdin.readline())

    student_grade = {}

    for _ in range(student_number):
        input_data = stdin.readline().split()
        student_grade[input_data[0]] = list(map(int, input_data[1:]))

    student_grade = sorted(student_grade.items(), key=lambda x: (-x[1][0], x[1][1], -x[1][2], x[0]))

    for name in student_grade:
        print(name[0])


if __name__ == "__main__":
    main()