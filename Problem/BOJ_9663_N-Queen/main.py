from sys import stdin

stdin = open("./input.txt", "r")
length_of_board = int(stdin.readline())
answer = [0]
visited = {}
for row in range(length_of_board):
    for col in range(length_of_board):
        visited["{}{}".format(row, col)] = 0


def process_visited(cur_row, cur_col, type):
    add_value = 1 if type == "visited" else -1
    for col in range(length_of_board):
        visited["{}{}".format(cur_row, col)] += add_value
    for row in range(length_of_board):
        visited["{}{}".format(row, cur_col)] += add_value

    # 오른쪽 아래
    next_row = cur_row + 1
    next_col = cur_col + 1
    while True:
        if next_row >= length_of_board or next_col >= length_of_board:
            break
        visited["{}{}".format(next_row, next_col)] += add_value
        next_row = next_row + 1
        next_col = next_col + 1
    # 왼쪽 위
    next_row = cur_row - 1
    next_col = cur_col - 1
    while True:
        if 0 > next_row or 0 > next_col:
            break
        visited["{}{}".format(next_row, next_col)] += add_value
        next_row = next_row - 1
        next_col = next_col - 1
    # 오른쪽 위
    next_row = cur_row - 1
    next_col = cur_col + 1
    while True:
        if 0 > next_row or next_col >= length_of_board:
            break
        visited["{}{}".format(next_row, next_col)] += add_value
        next_row = next_row - 1
        next_col = next_col + 1
    # 왼쪽 아래
    next_row = cur_row + 1
    next_col = cur_col - 1
    while True:
        if next_row >= length_of_board or 0 > next_col:
            break
        visited["{}{}".format(next_row, next_col)] += add_value
        next_row = next_row + 1
        next_col = next_col - 1


def positioning_queen(cur_queen, cur_row, cur_col, a, temp):
    process_visited(cur_row, cur_col, "visited")
    # print(visited)

    if cur_queen < length_of_board:
        for next_row in range(cur_row + 1, length_of_board):
            for next_col in range(length_of_board):
                if visited["{}{}".format(next_row, next_col)] == 0:
                    positioning_queen(cur_queen + 1, next_row, next_col, a, temp)

    if cur_queen == length_of_board:
        answer[0] += 1
    process_visited(cur_row, cur_col, "checkout")


def main():
    for col in range(length_of_board):
        if visited["{}{}".format(0, col)] == 0:
            positioning_queen(1, 0, col, [], [])
    print(answer[0])


if __name__ == '__main__':
    main()