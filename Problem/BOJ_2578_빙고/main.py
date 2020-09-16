from sys import stdin

def calling_number(bingo, number):
    row = 0
    col = 0
    for i in range(len(bingo)):
        for j in range(len(bingo[i])):
            if bingo[i][j] == number:
                row = i
                col = j
                bingo[i][j] = -1
    return [row, col]

def is_bingo(bingo, row, col):
    num_of_bingo = 0
    # 왼쪽 위 -> 오른쪽 아래
    for i in range(len(bingo)):
        if bingo[i][i] != -1:
            break
    else:
        num_of_bingo += 1

    # 오른쪽 위 -> 왼쪽 아래
    for i in range(len(bingo)):
        if bingo[i][len(bingo) - i - 1] != -1:
            break
    else:
        num_of_bingo += 1

    # 수평선
    for i in range(len(bingo)):
        one_row = bingo[i]
        for number in one_row:
            if number != -1:
                break
        else:
            num_of_bingo += 1

    # 수직선
    for i in range(len(bingo)):
        for j in range(len(bingo[i])):
            if bingo[j][i] != -1:
                break
        else:
            num_of_bingo += 1

    return num_of_bingo

def main():
    bingo = []
    called_number = []

    for _ in range(5):
        bingo.append(list(map(int, stdin.readline().split())))

    for _ in range(5):
        called_number.append(list(map(int, stdin.readline().split())))

    count = 0
    for i in range(len(called_number)):
        for j in range(len(called_number[i])):
            count += 1
            row, col = calling_number(bingo, called_number[i][j])
            if is_bingo(bingo, row, col) >= 3:
                print(count)
                return

    # for _ in range(5):
    #     called_numbers = list(map(int, stdin.readline().split()))
    #     for number in called_numbers:
    #         count += 1
    #         row, col = calling_number(bingo, number)
    #         if is_bingo(bingo, row, col) <= 3:
    #             print(count)
    #             return

if __name__ == '__main__':
    main()