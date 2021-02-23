from sys import stdin


moving_dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


def main():
    stdin = open("./input.txt", "r")
    rows, cols = map(int, stdin.readline().split())

    catholic_church = []
    for _ in range(rows):
        catholic_church.append(list(stdin.readline().rstrip()))

    seats = [[0] * cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if catholic_church[row][col] == "o":
                seats[row][col] = -1
                for moving_row, moving_col in moving_dir:
                    next_row = row + moving_row
                    next_col = col + moving_col
                    if 0 <= next_row < rows and 0 <= next_col < cols:
                        if seats[next_row][next_col] != -1:
                            seats[next_row][next_col] += 1

    count = 0
    answer_seat = (0, 0)
    for row in range(rows):
        for col in range(cols):
            if count < seats[row][col]:
                count = seats[row][col]
                answer_seat = (row, col)

    seats[answer_seat[0]][answer_seat[1]] = -1

    answer = 0
    for row in range(rows):
        for col in range(cols):
            if seats[row][col] == -1:
                for moving_row, moving_col in moving_dir:
                    next_row = row + moving_row
                    next_col = col + moving_col
                    if 0 <= next_row < rows and 0 <= next_col < cols:
                        if seats[next_row][next_col] == -1:
                            answer += 1
    print(answer // 2)


if __name__ == '__main__':
    main()