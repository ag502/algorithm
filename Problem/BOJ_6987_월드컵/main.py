from sys import stdin
from itertools import combinations


def cal_score(team1_score, team2_score, result):
    if result == "win":
        team1_score[0] += 1
        team2_score[2] += 1
    elif result == "lose":
        team1_score[2] += 1
        team2_score[0] += 1
    elif result == "draw":
        team1_score[1] += 1
        team2_score[1] += 1
    return team1_score, team2_score


def back_tracking(score_board, temp_score_board, comb_team, cur_idx, count):
    team1, team2 = comb_team[cur_idx]
    cur_team1_score = temp_score_board[team1]
    cur_team2_score = temp_score_board[team2]

    if cur_idx == len(comb_team) - 1:
        print(temp_score_board)
        return

    for next_idx in range(cur_idx + 1, len(comb_team)):
        for result in ["win", "lose", "draw"]:
            updated_team1_score, updated_team2_score = cal_score(cur_team1_score[:], cur_team2_score[:], result)
            if score_board[team1][0] >= updated_team1_score[0] and score_board[team1][1] >= updated_team1_score[1] and \
                    score_board[team1][2] >= updated_team1_score[2] \
                    and score_board[team2][0] >= updated_team2_score[0] and score_board[team2][1] >= \
                    updated_team2_score[1] and score_board[team2][2] >= updated_team2_score[2]:
                temp_score_board[team1] = updated_team1_score
                temp_score_board[team2] = updated_team2_score
                back_tracking(score_board, temp_score_board, comb_team, next_idx, count + 1)

    temp_score_board[team1] = cur_team1_score
    temp_score_board[team2] = cur_team2_score


def main():
    stdin = open("./input.txt", "r")

    score_boards = []
    for _ in range(4):
        score_board = []
        score = list(map(int, stdin.readline().split()))
        for idx in range(0, len(score) - 2, 3):
            score_board.append([score[idx], score[idx + 1], score[idx + 2]])
        score_boards.append(score_board)

    comb_teams = list(combinations([i for i in range(6)], 2))

    for score_board in score_boards:
        # print(score_board)
        temp_score_board = [[0, 0, 0] for _ in range(6)]
        back_tracking(score_board, temp_score_board, comb_teams, 0, 0)
        # print(temp_score_board)


if __name__ == '__main__':
    main()
