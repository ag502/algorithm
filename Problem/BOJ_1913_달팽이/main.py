from sys import stdin

moving_dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def main():
    stdin = open('./test_case.txt', 'r')
    n = int(stdin.readline())
    target_number = int(stdin.readline())
    snail = [[0] * n for _ in range(n)]
    target_pos = [0, 0]

    current_row = current_col = n // 2
    snail[current_row][current_col] = 1

    number = 2
    count = 0
    for i in range(1, n + 1):
        distance = i
        loop = 2
        if i == n:
            distance = i - 1
            loop = 1

        for j in range(loop):
            for k in range(distance):
                current_row += moving_dir[count % 4][0]
                current_col += moving_dir[count % 4][1]
                snail[current_row][current_col] = number
                if target_number == number:
                    target_pos[0] = current_row + 1
                    target_pos[1] = current_col + 1
                number += 1
            count += 1

    for row in snail:
        print(' '.join(map(str, row)))
    print(' '.join(map(str, target_pos)))

if __name__ == '__main__':
    main()