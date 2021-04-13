from sys import stdin
from copy import deepcopy

board = None
visited = [[False] * 3 for _ in range(3)]
answer = 0


def check_board():
    sum_of_board = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == "H":
                sum_of_board += 1
    return True if sum_of_board == 0 or sum_of_board == 9 else False


def dfs(temp_board):
    for row in temp_board:
        print(row)
    print("~~~~~~~~~~~")
    if check_board():
        global answer
        answer += 1

    for cur_row in range(3):
        for cur_col in range(3):
            # 행
            if not visited[cur_row][cur_col]:
                visited[cur_row][cur_col] = True
                for col in range(3):
                    if temp_board[cur_row][col] == "H":
                        temp_board[cur_row][col] = "T"
                    else:
                        temp_board[cur_row][col] = "H"
                dfs(temp_board)
                visited[cur_row][cur_col] = False
                temp_board = deepcopy(board)
                # 열
                for row in range(3):
                    if temp_board[row][cur_col] == "H":
                        temp_board[row][cur_col] = "T"
                    else:
                        temp_board[row][cur_col] = "H"
                dfs(temp_board)
                visited[cur_row][cur_col] = False
                temp_board = deepcopy(board)
                # 왼쪽 위 -> 오른쪽 아래
                start_row = cur_row - 2
                start_col = cur_col - 2
                while start_row != 2:
                    if 0 <= start_row < 3 and 0 <= start_col < 3:
                        if temp_board[start_row][start_col] == "H":
                            temp_board[start_row][start_col] = "T"
                        else:
                            temp_board[start_row][start_col] = "H"
                    start_row = start_row + 1
                    start_col = start_col + 1
                dfs(temp_board)
                visited[cur_row][cur_col] = False
                temp_board = deepcopy(board)

                # 오른쪽 위 -> 왼쪽 아래
                start_row = cur_row - 2
                start_col = cur_col + 2
                while start_row != 2:
                    if 0 <= start_row < 3 and 0 <= start_col < 3:
                        if temp_board[start_row][start_col] == "H":
                            temp_board[start_row][start_col] = "T"
                        else:
                            temp_board[start_row][start_col] = "H"
                    start_row += 1
                    start_col -= 1
                dfs(temp_board)
                visited[cur_row][cur_col] = False
                temp_board = deepcopy(board)


def main():
    stdin = open("./input.txt", "r")
    test_case = int(stdin.readline())

    for _ in range(test_case):
        global board
        global answer
        board = []
        answer = 0
        for i in range(3):
            board.append(stdin.readline().split())
        temp_board = deepcopy(board)
        dfs(temp_board)
        print(answer)


if __name__ == '__main__':
    main()