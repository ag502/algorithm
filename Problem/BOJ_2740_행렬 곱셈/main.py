from sys import stdin

def matrix_multiply(matrix_a, matrix_b):
    answer = []
    for a_row in matrix_a:
        row = []
        for b_col in zip(*matrix_b):
            temp = 0
            for a_num, b_num in zip(a_row, b_col):
                temp += a_num * b_num
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


