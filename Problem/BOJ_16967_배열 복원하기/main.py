from sys import stdin

def main():
    stdin = open('./test_case.txt', 'r')

    rows, cols, x, y = map(int, stdin.readline().split())
    array_b = []

    for _ in range(rows + x):
        row = list(map(int, stdin.readline().split()))
        array_b.append(row)

    answer = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if x <= i < rows and y <= j < cols:
                answer[i][j] = abs(array_b[i][j] - answer[i - x][j - y])
            else:
                answer[i][j] = array_b[i][j]

    for i in range(rows):
        print(' '.join(map(str, answer[i])))

if __name__ == '__main__':
    main()