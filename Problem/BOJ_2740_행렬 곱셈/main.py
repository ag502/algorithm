from sys import stdin

def matrix_multiply(matrix_a, matrix_b):
    answer = []
    for a_row in matrix_a:
        row = []
        for i in range(len(matrix_b[0])):
            temp = 0
            for idx, num in enumerate(a_row):
                temp += a_row[idx] * matrix_b[idx][i]
            row.append(temp)
        answer.append(row)

    return answer


def main():
    matrix_a = []
    matrix_b = []

    n, m = map(int, stdin.readline().split())
    for _ in range(n):
        row = list(map(int, stdin.readline().split()))
        matrix_a.append(row)

    m, k = map(int, stdin.readline().split())
    for _ in range(m):
        row = list(map(int, stdin.readline().split()))
        matrix_b.append(row)

    answer = matrix_multiply(matrix_a, matrix_b)

    for row in answer:
        for idx, num in enumerate(row):
            print(num, end='')
            if idx != len(row) - 1:
                print(' ', end='')
        print()

if __name__ == '__main__':
    main()


