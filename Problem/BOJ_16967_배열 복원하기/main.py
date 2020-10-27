from sys import stdin

def main():
    stdin = open('./test_case.txt', 'r')

    rows, cols, x, y = map(int, stdin.readline().split())
    array_b = []

    for _ in range(rows + x):
        row = list(map(int, stdin.readline().split()))
        array_b.append(row)

    array_a_1 = [[0] * cols for _ in range(rows)]
    array_a_2 = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            array_a_1[i][j] = array_b[i][j]

    for i in range(x, rows + x):
        for j in range(y, cols + y):
            array_a_2[i - x][j - y] = array_b[i][j]

    answer = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if array_a_1[i][j] == array_a_2[i][j]:
                answer[i][j] = array_a_1[i][j]
            else:
                answer[i][j] = abs(array_a_1[i][j] - array_a_2[i][j])

    print(answer)
    
if __name__ == '__main__':
    main()