from sys import stdin
from itertools import combinations

stdin = open("./input.txt", "r")
score_boards = []
for _ in range(4):
    score_boards.append(list(map(int, stdin.readline().split(" "))))

teams = list(combinations([i for i in range(6)], 2))
result = ["win", "lose", "draw"]
answer = [0, 0, 0, 0]


def cal_score(score_board, team1, team2, result, type):
    if result == "win":
        if type == "add":
            score_board[team1 * 3] += 1
            score_board[team2 * 3 + 2] += 1
        elif type == "restore":
            score_board[team1 * 3] -= 1
            score_board[team2 * 3 + 2] -= 1
    elif result == "lose":
        if type == "add":
            score_board[team1 * 3 + 2] += 1
            score_board[team2 * 3] += 1
        elif type == "restore":
            score_board[team1 * 3 + 2] -= 1
            score_board[team2 * 3] -= 1
    elif result == "draw":
        if type == "add":
            score_board[team1 * 3 + 1] += 1
            score_board[team2 * 3 + 1] += 1
        elif type == "restore":
            score_board[team1 * 3 + 1] -= 1
            score_board[team2 * 3 + 1] -= 1


def is_valid_score(score_board, cur_score, team1, team2):
    if score_board[team1 * 3] >= cur_score[team1 * 3] and score_board[team1 * 3 + 1] >= cur_score[team1 * 3 + 1] and score_board[team1 * 3 + 2] >= cur_score[team1 * 3 + 2] and \
            score_board[team2 * 3] >= cur_score[team2 * 3] and score_board[team2 * 3 + 1] >= cur_score[team2 * 3 + 1] and score_board[team2 * 3 + 2] >= cur_score[team2 * 3 + 2]:
        return True
    return False


def back_tracking(cur_score_idx, temp_score_board, cur_idx, result_idx, count):
    team1, team2 = teams[cur_idx]
    game_result = result[result_idx]

    cal_score(temp_score_board, team1, team2, game_result, "add")

    if count < 15:
        if is_valid_score(score_boards[cur_score_idx], temp_score_board, team1, team2):
            for next_idx in range(cur_idx + 1, len(teams)):
                for idx in range(len(result)):
                    back_tracking(cur_score_idx, temp_score_board, next_idx, idx, count + 1)

    if count == 15:
        if answer[cur_score_idx] == 1:
            return
        is_find = True
        for origin_score, temp_score in zip(score_boards[cur_score_idx], temp_score_board):
            if origin_score != temp_score:
                is_find = False
                break
        if is_find:
            answer[cur_score_idx] = 1
            return

    cal_score(temp_score_board, team1, team2, game_result, "restore")


def main():
    for idx in range(len(score_boards)):
        temp_score_board = [0] * 18
        for result_idx in range(len(result)):
            back_tracking(idx, temp_score_board, 0, result_idx, 1)
    print(' '.join(map(str, answer)))


if __name__ == '__main__':
    main()
